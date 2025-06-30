from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

loder=TextLoader('me.txt')
docs=loder.load()

model= OllamaLLM(model="mistral")

parser=StrOutputParser()

temp=PromptTemplate(
    template="write a main 5 a point about docs \n {docs}",
    input_variables=['docs']
)



chain=temp | model |parser
result=chain.invoke({'docs':docs[0].page_content})
print(result)

# print(type(docs))
# print(docs[0])