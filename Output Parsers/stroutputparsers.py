from langchain_community.llms import Ollama 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = Ollama(model="mistral")

template1=PromptTemplate(
    template="write a details about how to start {topic}",
    input_variables= ['topic']
)

tempalte2=PromptTemplate(
    template="write a 5 line summary on the text .\n{text}",
    input_variables=['text']
    
)

parse=StrOutputParser ()
chain=template1 | model | parse | tempalte2 |model |parse

result=chain.invoke({'topic':"about jumla nepal "})
print(result)
