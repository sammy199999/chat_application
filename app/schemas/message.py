from pydantic import BaseModel
from typing import List
from datetime import datetime

class MessageCreate(BaseModel):
    chat_id: str
    question: str
    response: str
    response_id: str
    timestamp: datetime

class MessageOut(BaseModel):
    chat_id: str
    question: str
    response: str
    response_id: str
    timestamp: datetime
    branches: List[str]