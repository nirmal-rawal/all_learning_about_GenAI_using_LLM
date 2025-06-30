from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ChatService:
    def __init__(self, model_name="mistral"):
        self.llm = Ollama(model=model_name)
        self.chat_history = []
        
    def get_response(self, user_input):
        # You can customize the prompt template as needed
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant."),
            *[(f"{'user' if i % 2 == 0 else 'ai'}", message) 
              for i, message in enumerate(self.chat_history[-6:])],  # Keep last 3 exchanges
            ("user", "{input}")
        ])
        
        chain = prompt | self.llm | StrOutputParser()
        
        response = chain.invoke({"input": user_input})
        
        # Update chat history
        self.chat_history.extend([user_input, response])
        
        return response

# Singleton instance
chat_service = ChatService()