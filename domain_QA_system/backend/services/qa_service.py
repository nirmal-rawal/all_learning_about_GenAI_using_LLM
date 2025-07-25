from typing import Optional
from backend.core.llm import LLMService
from backend.core.vector_db import VectorDB

class QAService:
    def __init__(self):
        self.llm = LLMService()
        self.vector_db = VectorDB()
    
    def answer_question(self, question: str) -> str:
        # Retrieve relevant documents
        results = self.vector_db.query(question)
        
        # Combine context
        context = "\n\n".join(results['documents'][0])
        
        # Generate answer
        answer = self.llm.generate(question, context)
        
        return answer, results['documents'][0]