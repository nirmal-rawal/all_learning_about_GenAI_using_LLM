from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text="jumla is the captial of karanli "
vec=embedding.embed_query(text)
print(vec)
