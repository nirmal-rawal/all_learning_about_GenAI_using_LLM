from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_community.llms import Ollama

# Initialize the LLM
llm = Ollama(model="mistral")

# Initialize the conversation with a system message and a human message
messages = [
    SystemMessage(content="You are a health expert."),
    HumanMessage(content="Tell me about common cold.")
]

# Get the AI's response
response = llm.invoke(messages)


# Append the AI's response to the messages
messages.append(AIMessage(content=response))


for mag in messages:
    if isinstance(mag,SystemMessage):
        print(f"System:{mag.content}")
        
    elif isinstance(mag,HumanMessage):
        print(f"User:{mag.content}")
    elif isinstance(mag,AIMessage):
        print(f"AImessage :{mag.content}")
# Print each message in a readable format
# print("\nFull conversation:")
# for msg in messages:
#     if isinstance(msg, SystemMessage):
#         print(f"System: {msg.content}")
#     elif isinstance(msg, HumanMessage):
#         print(f"Human: {msg.content}")
#     elif isinstance(msg, AIMessage):
#         print(f"AI: {msg.content}")