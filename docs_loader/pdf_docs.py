from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("2.pdf")

docs=loader.load()
# print(docs)
# print(len(docs))
print(docs[5].page_content)
print(docs[5].metadata)
