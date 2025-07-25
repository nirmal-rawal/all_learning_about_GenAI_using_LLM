import streamlit as st
from backend.services.qa_service import QAService
from backend.services.document_service import DocumentService
import os
import sys

import os
os.environ['STREAMLIT_TELEMETRY'] = 'False'
sys.path.append('/app')

# Initialize services
qa_service = QAService()
doc_service = DocumentService()

# Streamlit UI
st.title("Domain-Specific Q&A System")

# Sidebar for document upload
with st.sidebar:
    st.header("Document Management")
    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type=["pdf"],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Save the file temporarily
            with open(f"temp_{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Process and ingest the document
            documents = doc_service.process_pdf(f"temp_{uploaded_file.name}")
            doc_service.ingest_documents(documents)
            
            # Clean up
            os.remove(f"temp_{uploaded_file.name}")
            
        st.success(f"Processed {len(uploaded_files)} documents!")

# Main Q&A interface
question = st.text_input("Ask a question about your documents:")

if question:
    answer, sources = qa_service.answer_question(question)
    
    st.subheader("Answer")
    st.write(answer)
    
    with st.expander("See sources"):
        for i, source in enumerate(sources):
            st.write(f"Source {i+1}:")
            st.text(source[:500] + "...")  # Show first 500 chars