from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled  # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate



# 1️⃣ Get the YouTube transcript
video_id = "TmHVokqE-H8"  # Only the ID, not the full URL
try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    # print(transcript)
except TranscriptsDisabled:
    print("No captions available for this video.")
    transcript = ""
    
embedding_model = OllamaEmbeddings(model="mistral")
generation_model = OllamaLLM(model="mistral")

splitter=RecursiveCharacterTextSplitter(
    chunk_size=3000,
    chunk_overlap=500
)

chunk=splitter.create_documents([transcript])
# print(len(chunk))
# print(chunk)

vector_store=FAISS.from_documents(chunk,embedding_model)


retriever=vector_store.as_retriever(
      search_type='similarity',
    search_kwargs={'k':4}
)

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
# final_prompt=prompt.invoke({'context':content_text,'topic':topic})

def format_docs(retriever_docs):
    content_text="\n\n".join(doc.page_content for doc in retriever_docs)
    return content_text

parallel_chain=RunnableParallel({
    'context':retriever | RunnableLambda(format_docs),
    'topic':RunnablePassthrough()
})
result=parallel_chain.invoke("tell me  about meditations")

parser=StrOutputParser()

main_chain=parallel_chain |prompt | generation_model | parser
result=main_chain.invoke("in this vidoe they are talk about meditations? if yes what was disscussed?")
print(result)

