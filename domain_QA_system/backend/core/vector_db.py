import chromadb
from chromadb.utils import embedding_functions
from backend.config.settings import settings

class VectorDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=settings.embedding_model
        )
        self.collection = self.client.get_or_create_collection(
            name=settings.collection_name,
            embedding_function=self.embedding_func
        )
    
    def add_documents(self, documents: list, metadatas: list = None, ids: list = None):
        if metadatas is None:
            metadatas = [{} for _ in documents]
        if ids is None:
            ids = [str(i) for i in range(len(documents))]
        
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    
    def query(self, query_text: str, n_results: int = 3):
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results