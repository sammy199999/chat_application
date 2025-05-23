from pydantic import BaseModel
from typing import List

class BranchCreate(BaseModel):
    base_chat_id: str
    response_id: str
    new_branch_id: str

class BranchSetActive(BaseModel):
    chat_id: str
    branch_id: str