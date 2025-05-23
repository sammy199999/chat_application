from pydantic import BaseModel
from typing import List
from datetime import datetime

class QAPair(BaseModel):
    question: str
    response: str
    response_id: str
    timestamp: datetime
    branches: List[str] = []

class ChatContent(BaseModel):
    chat_id: str
    qa_pairs: List[QAPair]