from langchain_community.tools import StructuredTool
from pydantic import BaseModel,Field

class MultyplyClass(BaseModel):
    a:int =Field(requierd=True,description="Enter the first number") # type: ignore
    b:int =Field(requierd=True,description="Enter the second number") # type: ignore

def multi(a,b):
    return a *b

custom_tool=StructuredTool.from_function(
    func=multi,
    name="multiply",
    description="This tool multiplies two numbers together",
    args_schema=MultyplyClass
)

print(custom_tool.invoke({'a':4,'b':6}))
print(custom_tool.name)
print(custom_tool.description)