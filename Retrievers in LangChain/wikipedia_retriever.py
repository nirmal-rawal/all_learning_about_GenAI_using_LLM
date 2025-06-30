from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever
retriever = WikipediaRetriever(top_k_results=2, lang="en") # type: ignore

# Define your query
query = "history of Nepal where Nepali Gorkhali war with British, India, and China"

# Call invoke correctly
docs = retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"\n--- Result{i+1}---")
    print(f"content:\n{doc.page_content}---")


