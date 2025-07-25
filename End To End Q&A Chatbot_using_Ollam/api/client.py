import streamlit as st
import os
import requests


import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY") # type: ignore

def get_response_ollama(input_txt):
    response=requests.post("http://localhost:8000/essay/invoke",
                  json={'input':{"topic": input_txt}})
    
    return response.json()['output']

st.title('Langchain Demo With mistral API')
input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(get_response_ollama(input_text))
