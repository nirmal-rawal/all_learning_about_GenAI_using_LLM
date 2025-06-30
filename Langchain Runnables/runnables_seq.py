from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


model= OllamaLLM(model="mistral")

parser=StrOutputParser()

promt=PromptTemplate(
    template="write a joke in satricale way about the {topic}",
    input_variables=['topic']
)

promt2=PromptTemplate(
    template="explain that following joke {topic} ",
    input_variables=['topic']
)

chain=RunnableSequence(promt|model|parser|promt2|model|parser)
user_input=input("user: ")

result=chain.invoke({'topic':user_input})
print(result)