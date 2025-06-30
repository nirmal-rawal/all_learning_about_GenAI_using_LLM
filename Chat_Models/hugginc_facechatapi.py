from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load .env and get token
load_dotenv()
hf_token = os.getenv("HF_API_TOKEN")

if not hf_token:
    raise ValueError("HF_API_TOKEN not found in environment variables.")

# Correct parameter: use model_kwargs instead of pipeline_kwargs
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    temperature=0.5, # type: ignore
    max_new_tokens=10
    
)

# Generate response
response = llm.invoke("total populations of jumla nepal? ?")

# Output
print(response)
