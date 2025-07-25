from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ollama_model: str = "mistral"
    embedding_model: str = "sentence-transformers/all-mpnet-base-v2"
    chunk_size: int = 1000
    chunk_overlap: int = 200
    collection_name: str = "document_qa"
    
    class Config:
        env_file = ".env"

settings = Settings()