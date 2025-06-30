# from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Load environment variables
# load_dotenv(override=True)

# # Verify token
# hf_token = os.getenv("HF_API_TOKEN")
# if not hf_token or not hf_token.startswith("hf_"):
#     logger.error("Invalid or missing Hugging Face token!")
#     raise ValueError("Please check your HF_API_TOKEN in .env file")

# # Initialize LLM with enhanced settings
# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-7B-Instruct-v0.1",
#     task="text-generation",
#     huggingfacehub_api_token=hf_token,
#     temperature=0.7,
#     max_new_tokens=200,
#     top_p=0.9,
#     top_k=40,
#     timeout=60,  # Increased timeout
#     model_kwargs={
#         "device_map": "auto",
#         "trust_remote_code": True
#     }
# )

# logger.info("✅ LLM initialized successfully with Mistral-7B")