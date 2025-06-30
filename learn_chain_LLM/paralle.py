from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import Anthropic
from langchain.schema.runnable import RunnableParallel

model= OllamaLLM(model="mistral")
model2=Anthropic(model_name='claude-3')
parse=StrOutputParser()

promt1=PromptTemplate(
    template="generat a short and simple note from the following text \n {text}",
    input_variables=['text'],
    
)

promt2=PromptTemplate(
    template="Generae a 5 question answer  from the following text \n {text}",
    input_variables=['text'],
)

prompt3=PromptTemplate(
    template="marge the provided notes and quize into a single document \n notes -> {notes} and {quize}",
    input_variables=['notes','quize'],
)

parallel_chain= RunnableParallel({
    'notes': promt1 | model |parse,
    "quize": promt2 | model2 |parse
})  

merge_chain= prompt3 |model | parse 

final_chain= parallel_chain | merge_chain
text= """
Generative AI models use neural networks to identify the patterns and structures within existing data to generate new and original content.

One of the breakthroughs with generative AI models is the ability to leverage different learning approaches, including unsupervised or semi-supervised learning for training. This has given organizations the ability to more easily and quickly leverage a large amount of unlabeled data to create foundation models. As the name suggests, foundation models can be used as a base for AI systems that can perform multiple tasks. 

Examples of foundation models include GPT-3 and Stable Diffusion, which allow users to leverage the power of language. For example, popular applications like ChatGPT, which draws from GPT-3, allow users to generate an essay based on a short text request. On the other hand, Stable Diffusion allows users to generate photorealistic images given a text input.
"""

respose = final_chain.invoke({'text':text})
print(respose)