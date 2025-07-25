import pytest
from backend.services.document_service import DocumentService
from backend.services.qa_service import QAService
import os

@pytest.fixture
def sample_pdf(tmp_path):
    from fpdf import FPDF
    
    pdf_path = tmp_path / "test.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test PDF document.", ln=True, align='C')
    pdf.output(pdf_path)
    return pdf_path

def test_full_rag_flow(sample_pdf):
    # Ingest document
    doc_service = DocumentService()
    documents = doc_service.process_pdf(str(sample_pdf))
    doc_service.ingest_documents(documents)
    
    # Query
    qa_service = QAService()
    answer, sources = qa_service.answer_question("What is this document about?")
    
    assert isinstance(answer, str)
    assert len(answer) > 0
    assert len(sources) > 0
    assert "test PDF document" in sources[0]