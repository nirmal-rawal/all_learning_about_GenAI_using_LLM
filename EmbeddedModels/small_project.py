from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

# Load environment variables
load_dotenv()

# Initialize embedding model (remove unsupported 'dimensions' argument)
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Query
query = "Tell me about Sachin Tendulka"

# Get embeddings
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Compute and print cosine similarity
similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0] # type: ignore
index,score=sorted(list(enumerate(similarity_scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("smalarity_score:",score)
