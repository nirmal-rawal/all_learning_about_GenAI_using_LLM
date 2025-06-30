# Sample documents
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS


model_emb = OllamaEmbeddings(model="mistral")
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

vectro_sote=FAISS.from_documents(
    documents=docs,
    embedding=model_emb
)

retrivers=vectro_sote.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3,"lambda_mult":0.5}
    
)
query="what is langchina"
restul=retrivers.invoke(query)
for i,doc in enumerate(restul):
    print(f'resutl {i+1}')
    print(f'Content : {doc.page_content}')