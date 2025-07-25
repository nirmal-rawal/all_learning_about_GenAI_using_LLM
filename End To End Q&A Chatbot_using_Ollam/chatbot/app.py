from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY") # type: ignore

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Langchain Demo With mistral API')
input_text=st.text_input("Search the topic u want")

# ollama LLAma2 LLm 
llm=OllamaLLM(model="mistral")
output_parser=StrOutputParser()
chain=prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))