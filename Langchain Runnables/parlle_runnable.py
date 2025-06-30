from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel


model= OllamaLLM(model="mistral")

parser=StrOutputParser()

Promt1= PromptTemplate(
    template="generate a twitter post about {topic}",
    input_variables=['topic']   
)
Promt2= PromptTemplate(
    template="generate a linkdin post about {topic}",
    input_variables=['topic']   
)

chain=RunnableParallel(
    {
        "twitter":RunnableSequence(Promt1|model|parser),
        "linkedin":RunnableSequence(Promt2|model|parser),
    }
)
user_input=input('user:')
result=chain.invoke({'topic':user_input})
print(result)

