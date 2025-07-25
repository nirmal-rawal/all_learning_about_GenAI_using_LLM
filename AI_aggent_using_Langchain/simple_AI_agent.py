from langchain_ollama import OllamaLLM
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
import requests


search_tool=DuckDuckGoSearchRun()
llm=OllamaLLM(model='mistral')

@tool
def featch_weather_data(city:str)->str:
    """this function will fetch the weather data of a given city"""
    url=f"https://api.weatherstack.com/current?access_key=b71f6045c8c3cde20cc7547900a917d6&query={city}"
    result=requests.get(url)
    return result.json()
    
    
    
#pull the react prompt form the hub
prompt=hub.pull("hwchase17/react")

#create a react agent manully with the pulled prompt 
agent=create_react_agent(
    llm=llm,
    tools=[search_tool,featch_weather_data],
    prompt=prompt
)

#wrap with a AgentExuturo 
executor=AgentExecutor(
    agent=agent,
    tools=[search_tool,featch_weather_data],
    verbose=True,
    handle_parsing_errors=True
)

response=executor.invoke({'input':"where is Karnali Academy of Health Sciences (KAHS) located  and what is the weather like there?"
                        })
print(response)
