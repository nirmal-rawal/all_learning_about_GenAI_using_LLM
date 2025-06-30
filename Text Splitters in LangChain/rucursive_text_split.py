from langchain.text_splitter import RecursiveCharacterTextSplitter

text="""Dear Student Services Team,

I hope this message finds you well.

I am writing to kindly request an official attendance report for all modules of my Level 5 and Level 6 studies. This report is required as part of my scholarship application, which includes verification of attendance across both levels.

I would be grateful if you could prepare and share the verified attendance report at your earliest convenience. Please let me know if any additional information or documents are needed from my side to process this request.
"""
rescu=RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=5
)

result= rescu.split_text(text)
print(result)
print(len(result))