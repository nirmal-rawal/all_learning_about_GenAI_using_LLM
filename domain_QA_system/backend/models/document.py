from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    id: str
    content: str
    metadata: Optional[dict] = None