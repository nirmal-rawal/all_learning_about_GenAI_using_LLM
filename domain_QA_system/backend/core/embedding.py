from sentence_transformers import SentenceTransformer
from backend.config.settings import settings

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(settings.embedding_model)
    
    def embed(self, text: str):
        return self.model.encode(text)