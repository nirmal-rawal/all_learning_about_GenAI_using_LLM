# Start your code here!
import os
from langchain_community.llms import Ollama 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage, SystemMessage

# Define the model to use
model = Ollama(model="mistral")

converation=[
    {'role':'system','content':" you are the travel expert who know everything about Paris. Answer concisely and accurately."}
]

while True:
    user_input=input("you :")
    if user_input.lower() in ['quit','exit']:
        break
    converation.append({'role':"user",'content':user_input})
    response=model.invoke(user_input)
    
    converation.append({'role':'Assistant',"contnet":response})
    print("assistant :" ,response)

for message in converation:
    if message['role'] == 'system':
        print(message)
    elif message['role']=='user':
        print(message)
    elif message['role']=='Assistant':
        print(message)