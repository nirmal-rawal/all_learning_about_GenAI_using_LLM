from langchain_community.llms import Ollama 
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
model = Ollama(model="mistral")

class Person(BaseModel):
    name:str
    age:int
    city:str
    
    
parse=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate a name ,age and city of a fictional {place} person \n {format_insturaction}",
    input_variables=['place'],
    partial_variables={'format_insturaction':parse.get_format_instructions()}
    
)

chain=template | model | parse

prompt= chain.invoke({'place':"from Nepal"})
print(prompt)
print(prompt)