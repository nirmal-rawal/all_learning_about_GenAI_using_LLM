from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


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

joke_generator=promt|model|parser
par_chain=RunnableParallel({
    'joke': joke_generator,
    'explantions':RunnableSequence(promt2|model|parser)
})

final_chain= RunnableSequence(joke_generator,par_chain
                              )
result =final_chain.invoke({'topic':'kp oli'})
print(result)
