#Built-in Tool - DuckDuckGo Search
from langchain_community.tools import DuckDuckGoSearchRun

doc=DuckDuckGoSearchRun()
result=doc.invoke("top news in nepal today")
# print(result)

#Built in tool shell tool

from langchain_community.tools import ShellTool

tool=ShellTool()
print(tool.invoke('whoami '))

