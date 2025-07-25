from langchain_community.tools import tool

@tool
def division(a: int, b: int) -> float:
    """This tool divides the numbers."""
    return a / b

result = division.invoke({"a": 15, "b": 5})
print(result)
print(division.name)
print(division.description)
print(division.args)