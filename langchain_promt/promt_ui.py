from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()


st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template=load_prompt('template.json')

if st.button("Summarize"):
    chain=template | llm  # type: ignore
    response=chain.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})
    
    st.write(response)