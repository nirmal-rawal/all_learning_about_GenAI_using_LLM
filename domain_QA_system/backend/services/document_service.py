from typing import List
from pypdf import PdfReader
from backend.models.document import Document
from backend.core.vector_db import VectorDB
from backend.config.settings import settings

class DocumentService:
    def __init__(self):
        self.vector_db = VectorDB()
    
    def process_pdf(self, file_path: str) -> List[Document]:
        reader = PdfReader(file_path)
        documents = []
        
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                documents.append(Document(
                    id=f"page_{page_num}",
                    content=text,
                    metadata={"source": file_path, "page": page_num}
                ))
        
        return documents
    
    def chunk_document(self, document: Document) -> List[Document]:
        text = document.content
        chunks = []
        
        start = 0
        while start < len(text):
            end = min(start + settings.chunk_size, len(text))
            chunk = text[start:end]
            
            chunks.append(Document(
                id=f"{document.id}_chunk_{len(chunks)}",
                content=chunk,
                metadata=document.metadata
            ))
            
            start = end - settings.chunk_overlap
        
        return chunks
    
    def ingest_documents(self, documents: List[Document]):
        chunks = []
        for doc in documents:
            chunks.extend(self.chunk_document(doc))
        
        self.vector_db.add_documents(
            documents=[chunk.content for chunk in chunks],
            metadatas=[chunk.metadata for chunk in chunks],
            ids=[chunk.id for chunk in chunks]
        )