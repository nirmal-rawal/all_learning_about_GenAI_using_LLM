from langchain_ollama import OllamaLLM
from langchain_community.tools import tool
from langchain_core.messages import HumanMessage

@tool
def multiply(a: int, b: int) -> int:
    """Multiplication of two integers"""
    return a * b

llm = OllamaLLM(model="mistral")

# ✅ Correct method name: bind_tools (plural!)
llm_with_binding = llm.bind_tools([multiply]) # type: ignore

# Example usage (optional):
response = llm_with_binding.invoke([HumanMessage(content="What is 3 times 5?")])
print(response)
