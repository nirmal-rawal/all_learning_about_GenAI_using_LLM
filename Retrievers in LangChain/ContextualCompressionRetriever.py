from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document


model_emb = OllamaEmbeddings(model="mistral")

docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})
]

vector_store=FAISS.from_embeddings(docs,model_emb)# type: ignore

base_retrievers=vector_store.as_retriever(search_kwargs={'k':2})
compessor=LLMChainExtractor.from_llm(model_emb) # type: ignore
context_retr=ContextualCompressionRetriever(
    base_retriever=base_retrievers,
    base_compressor=compessor
)

query="what is photosynthithis?"
compessor_result=context_retr.invoke(query)

for i, doc in enumerate(compessor_result):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
