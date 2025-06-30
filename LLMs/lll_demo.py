from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Get OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

# Set the OpenAI client base URL for OpenRouter
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key, # type: ignore
)

# Invoke the model
response = llm.invoke([
    HumanMessage(content="capital city of nepal ")
])

print(response)
