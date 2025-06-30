from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

lo=PyPDFLoader("dl-curriculum.pdf")
docs=lo.load()
spli=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
res =spli.split_documents(docs)
print(res[5])