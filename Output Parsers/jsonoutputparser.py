from langchain_community.llms import Ollama 
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate

model = Ollama(model="mistral")

parser=JsonOutputParser()
tem=PromptTemplate(
    template='give me the name of name, age and city of the alice person  \n {format_insturaction}',
    input_variables=[],
    partial_variables={'format_insturaction':parser.get_format_instructions()}
    
)
chain=tem | model | parser 
final_result=chain.invoke({})
print(final_result)