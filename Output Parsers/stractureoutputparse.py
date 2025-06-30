from langchain_community.llms import Ollama 
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate

model = Ollama(model="mistral")

schema=[
    ResponseSchema(name='fact_1',description='fact about the topic'),
    ResponseSchema(name='fact_2',description='fact about the topic'),
    ResponseSchema(name='fact_3',description='fact about the topic'),
    ResponseSchema(name='fact_4',description='fact about the topic'),
    ResponseSchema(name='fact_5',description='fact about the topic')
]
parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="give me the top 5 fact about{topic}\n {format_instruction}",
    input_variables=['topic'],
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)
chain=template | model |parser 
promt=template.invoke({'topic':"all about jumla Nepal"})

final_result= chain.invoke(promt)
print(final_result)

