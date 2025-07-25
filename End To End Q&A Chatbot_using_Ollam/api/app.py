from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes # type: ignore
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Use the updated Ollama import
from langchain_community.llms import Ollama
llm = Ollama(model="mistral")

# Add output parser to ensure string output
chain = llm | StrOutputParser()

add_routes(
    app,
    chain,
    path="/openai"
)

prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Write an essay about the {topic} with 200 words.")
])

# Combine prompt and llm with output parser
essay_chain = prompt1 | llm | StrOutputParser()

add_routes(
    app,
    essay_chain,
    path="/essay"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)