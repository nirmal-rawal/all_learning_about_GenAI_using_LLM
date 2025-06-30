from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = OllamaLLM(model="mistral")

parse=StrOutputParser()

prompt1= PromptTemplate(
    template="give me the details repoert about the {topic}",
    input_variables=['topic']
)

promt2=PromptTemplate(
    template="genereatea a 5 point summary of the following text \n {text}",
    input_variables=['text']
    
)

chain=prompt1 | model |parse | promt2 |model | parse

response =chain.invoke({'topic':"AI"})

print(response)