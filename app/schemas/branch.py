from pydantic import BaseModel, field_validator
from typing import List

class BranchCreate(BaseModel):
    base_chat_id: str
    response_id: str
    new_branch_id: str

    @field_validator("base_chat_id", "response_id", "new_branch_id")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

class BranchSetActive(BaseModel):
    chat_id: str
    branch_id: str

    @field_validator("chat_id", "branch_id")
    @classmethod
    def not_empty(cls, v, field):
        if not v or not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v