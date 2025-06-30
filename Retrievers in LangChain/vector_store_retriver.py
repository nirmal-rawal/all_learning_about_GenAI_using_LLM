from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

# Step 2: Embedding model
model_emb = OllamaEmbeddings(model="mistral")

# Step 3: Create vector store
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=model_emb,
    collection_name="my_vec"
)

# Step 4: Make a retriever
retriever = vector_store.as_retriever(search_kwargs={'k': 2})

# Step 5: Query
query = "what is chroma used for"
result = retriever.invoke(query)

# ✅ Correct: loop over results, not original documents
for i, doc in enumerate(result):
    print(f"\n--- Result {i+1} ---")
    print(f"Content: {doc.page_content}")
