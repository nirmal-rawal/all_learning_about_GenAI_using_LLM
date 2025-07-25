import pytest
from unittest.mock import MagicMock, patch
from backend.services.qa_service import QAService

@pytest.fixture
def mock_qa_service():
    with patch('backend.core.llm.LLMService') as mock_llm, \
         patch('backend.core.vector_db.VectorDB') as mock_db:
        
        mock_db_instance = mock_db.return_value
        mock_db_instance.query.return_value = {
            'documents': [['Test context 1', 'Test context 2']]
        }
        
        mock_llm_instance = mock_llm.return_value
        mock_llm_instance.generate.return_value = "Test answer"
        
        service = QAService()
        yield service

def test_answer_question(mock_qa_service):
    answer, sources = mock_qa_service.answer_question("Test question")
    assert answer == "Test answer"
    assert len(sources) == 2
    assert "Test context 1" in sources