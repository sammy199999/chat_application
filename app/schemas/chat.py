from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from datetime import datetime

class ChatType(str, Enum):
    personal = "personal"
    group = "group"

class ChatCreate(BaseModel):
    account_id: str
    chat_type: ChatType
    name: str

class ChatUpdate(BaseModel):
    name: str

class ChatOut(BaseModel):
    chat_id: UUID
    account_id: str
    chat_type: ChatType
    name: str
    created_at: datetime
    updated_at: datetime
    active: bool