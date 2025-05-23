from fastapi import APIRouter, Depends
from app.schemas.branch import BranchCreate, BranchSetActive
from app.crud.branch import create_branch, get_all_branches
from app.db.mongo import get_mongo_client

router = APIRouter()

@router.post("/create-branch")
async def create_branch_view(data: BranchCreate, mongo_client=Depends(get_mongo_client)):
    await create_branch(mongo_client, data.base_chat_id, data.response_id, data.new_branch_id)
    return {"msg": "Branch created"}

@router.get("/get-branches")
async def get_branches_view(chat_id: str, mongo_client=Depends(get_mongo_client)):
    branches = await get_all_branches(mongo_client, chat_id)
    return {"branches": branches}

@router.put("/set-active-branch")
async def set_active_branch(data: BranchSetActive):
    # This would typically interact with SQL to mark the active branch
    return {"msg": f"Branch {data.branch_id} set as active for chat {data.chat_id}"}