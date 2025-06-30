from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal



class Feedback(BaseModel):
    sentiment: Literal['positive','negative','Neutral']= Field(description="give the sentiment of the feed back")
    
parser2=PydanticOutputParser(pydantic_object=Feedback)
model= OllamaLLM(model="mistral")

parser=StrOutputParser()

promt1=PromptTemplate(
    template="analysis the sentiment of the following feedback into postivie, negative or neutral \n {reviews} \n {format_instuction}",
    input_variables=['reviews'],
    partial_variables={'format_instuction':parser2.get_format_instructions()}
)

analysis_chain=promt1 |model |parser2

promtp2=PromptTemplate(
    template="write an appripate response to this positve feedback \n {reviews}",
    input_variables=['reviews'],
    
)
promtp3=PromptTemplate(
    template="write an appripate response to this negative feedback \n {reviews}",
    input_variables=['reviews'],
    
)
promtp4=PromptTemplate(
    template="write an appripate response to this Neutral feedback \n {reviews}",
    input_variables=['reviews'],
    
)


brach_chian=RunnableBranch(
    (lambda x:x.sentiment =='positive', promtp2 |model |parser), # type: ignore
    (lambda x:x.sentiment=='negative', promtp3 |model |parser), # type: ignore
    (lambda x:x.sentiment=='neutra', promtp4 |model |parser), # type: ignore
    RunnableLambda(lambda X:"could not fid the sentiment")
    
    
)

final= analysis_chain | brach_chian

result=final.invoke({'reviews':"It’s okay — not the best, but not the worst either. It does the job, but I didn’t find anything particularly special about it. Might work well for some people this is Neutral reviews"})
print(result)
final.get_graph().print_ascii()