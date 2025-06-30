from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled  # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# 1️⃣ Get the YouTube transcript
video_id = "5t1vTLU7s40"  # Only the ID, not the full URL
try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
except TranscriptsDisabled:
    print("No captions available for this video.")
    transcript = ""

# 2️⃣ Split the transcript
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.create_documents([transcript])
# print(f"Total Chunks: {len(chunks)}")

# 3️⃣ Create embeddings and store in vector store
embedding_model = OllamaEmbeddings(model="mistral")
generation_model = OllamaLLM(model="mistral")

vector_store = FAISS.from_documents(chunks, embedding_model)

# 4️⃣ Debug: Check index-to-docstore ID mapping and docstore keys
# print("\n📌 FAISS index_to_docstore_id:")
# print(vector_store.index_to_docstore_id)

# print("\n📌 Docstore keys:")
# print(vector_store.docstore._dict.keys())

# 5️⃣ Pick a valid ID and retrieve the chunk
# ✅ Always use a valid ID from the docstore
# valid_ids = list(vector_store.docstore._dict.keys())
# print("\n📌 Using valid ID:", valid_ids[0])

# result = vector_store.get_by_ids([valid_ids[0]])
# print("\n📌 Retrieved chunk content:")
# print(result)



                            #Retriever
                            
retriever=vector_store.as_retriever(
    search_type='similarity',
    search_kwargs={'k':4}
)

result=retriever.invoke('what is Open Source?')

# Augementations

prompt=PromptTemplate(
    template="""
    you are helpfull assisstance .
    answer only the form provided transcript context.
    if is the context is insufficent to answer the question. i don't know about {topic}.
    {context}
    question:{topic} 
    """,
    input_variables=['context','topic']
    
)

topic="in this topic limit of llm in this vidoe ? if yes what was discuessed"
retriever_docs=retriever.invoke(topic)
content_text="\n\n".join(doc.page_content for doc in retriever_docs)
final_prompt=prompt.invoke({'context':content_text,'topic':topic})


#Generation

answer=generation_model.invoke(final_prompt)
print(answer)

