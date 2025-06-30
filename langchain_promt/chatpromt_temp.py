from langchain_core.prompts import ChatPromptTemplate

# Define the chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in {domain}."),
    ("human", "Give me ideas about {topic}.")
])

# Provide the input values
prompt = chat_template.invoke({
    "domain": "content creation",
    "topic": "my cup business"
})

print(prompt)
