from pydantic import BaseModel, field_validator
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

    @field_validator("account_id", "name")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

class ChatUpdate(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

class ChatOut(BaseModel):
    chat_id: UUID
    account_id: str
    chat_type: ChatType
    name: str
    created_at: datetime
    updated_at: datetime
    active: bool

    @field_validator("account_id", "name")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v