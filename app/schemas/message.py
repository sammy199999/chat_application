from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime

class MessageCreate(BaseModel):
    chat_id: str
    question: str
    response: str
    response_id: str
    timestamp: datetime

    @field_validator("chat_id", "question", "response", "response_id")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

class MessageOut(BaseModel):
    chat_id: str
    question: str
    response: str
    response_id: str
    timestamp: datetime
    branches: List[str]

    @field_validator("chat_id", "question", "response", "response_id")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

    @field_validator("branches")
    @classmethod
    def branches_are_strings(cls, v):
        if not isinstance(v, list):
            raise ValueError("branches must be a list")
        for branch in v:
            if not isinstance(branch, str):
                raise ValueError("Each branch must be a string")
        return v