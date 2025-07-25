import ollama
from backend.config.settings import settings

class LLMService:
    def __init__(self):
        self.model = settings.ollama_model
    
    def generate(self, prompt: str, context: str = ""):
        full_prompt = f"Context: {context}\n\nQuestion: {prompt}\n\nAnswer:"
        response = ollama.generate(
            model=self.model,
            prompt=full_prompt,
            stream=False
        )
        return response['response']