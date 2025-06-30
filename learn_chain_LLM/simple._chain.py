from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = Ollama(model="mistral")
parse=StrOutputParser()

prompt=PromptTemplate(
    template="give me the 5 intereset fact about the {topic}",
    input_variables=['topic']
    
)
chain= prompt | model | parse

response=chain.invoke({'topic':"all about Jumla Nepal"})
print(response)
chain.get_graph().print_ascii()