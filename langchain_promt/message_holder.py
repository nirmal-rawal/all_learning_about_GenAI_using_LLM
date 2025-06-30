from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

chat_temp=ChatPromptTemplate([
    ('system',"you are the helpful customebr service of a company agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]
with open('chat_history.txt')as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

promt=chat_temp.invoke({'chat_history':chat_history,'query':"when my refund back?"})  
    

print(promt)