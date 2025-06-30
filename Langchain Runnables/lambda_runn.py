from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnableLambda,RunnablePassthrough


model= OllamaLLM(model="mistral")
def word_count(text):
    return len(text.split())

parser=StrOutputParser()

prompt=PromptTemplate(
    template="create the poem about the {topic}",
    input_variables=['topic']
)

poem_jok_gen=RunnableSequence(prompt|model|parser)

parallel_chain=RunnableParallel({
    'poem':poem_jok_gen,
    'word_count':RunnableLambda(word_count)
}
)


final_chain=RunnableSequence(poem_jok_gen,parallel_chain)

res=final_chain.invoke({"topic":"politic"})
print(res['poem'])
print(res['word_count'])