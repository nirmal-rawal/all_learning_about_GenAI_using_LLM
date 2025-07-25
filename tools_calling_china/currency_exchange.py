#tool Create
from langchain_community.tools import tool
from langchain_ollama import OllamaLLM
import requests
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage


@tool
def conversion_rate(base_currency:str,target_currency:str) ->float:
    """Calculate the conversion rate between two currencies."""
    url=f"https://v6.exchangerate-api.com/v6/ab2319f80b0dff2da6530457/pair/{base_currency}/{target_currency}"
    response =requests.get(url)
    return response.json()

conv=conversion_rate.invoke({'base_currency':'USD','target_currency':"NPR"})
# print(conv)


@tool
def convert_currency(base_currancy_value:int,conv_rate:float)->float:
    """Convert the base currency value to the target currency using the conversion rate."""
    return base_currancy_value * conv_rate

input=convert_currency.invoke({'base_currancy_value':15,'conv_rate':137.2016})
# print(input)

llm=OllamaLLM(model="mistral")
llm_with_tools = llm.bind_tools([conversion_rate, convert_currency]) # type: ignore
messages = [HumanMessage('What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd')]

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

import json
for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'conversion_rate':
        tool_message1=conversion_rate.invoke(tool_call)
         # fetch this conversion rate
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        # append this tool message to messages list
        messages.append(tool_message1)
    # execute the 2nd tool using the conversion rate from tool 1
    if tool_call['name'] == 'convert':
        # fetch the current arg
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert_currency.invoke(tool_call)
        messages.append(tool_message2)
        
llm_with_tools.invoke(messages).content
        


    