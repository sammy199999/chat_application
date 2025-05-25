from fastapi import APIRouter, Depends, HTTPException
from app.schemas.branch import BranchCreate, BranchSetActive
from app.crud.branch import create_branch, get_all_branches
from app.db.mongo import get_mongo_client
from app.auth.auth import get_api_key


router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post("/create-branch")
async def create_branch_view(data: BranchCreate, mongo_client=Depends(get_mongo_client)):
    """
    Create a new branch for a chat.
    Args:
        data (BranchCreate): Data required to create a branch.
        mongo_client: MongoDB client dependency.
    Returns:
        dict: Success message.
    Raises:
        HTTPException: If branch creation fails.
    """
    try:
        await create_branch(mongo_client, data.base_chat_id, data.response_id, data.new_branch_id)
        return {"msg": "Branch created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create branch: {str(e)}")

@router.get("/get-branches")
async def get_branches_view(chat_id: str, mongo_client=Depends(get_mongo_client)):
    """
    Retrieve all branches for a given chat.
    Args:
        chat_id (str): ID of the chat to retrieve branches for.
        mongo_client: MongoDB client dependency.
    Returns:
        dict: Dictionary containing list of branches.
    Raises:
        HTTPException: If retrieval fails.
    """
    try:
        branches = await get_all_branches(mongo_client, chat_id)
        return {"branches": branches}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get branches: {str(e)}")

@router.put("/set-active-branch")
async def set_active_branch(data: BranchSetActive):
    """
    Set a branch as active for a chat.
    Args:
        data (BranchSetActive): Data containing chat and branch IDs.
    Returns:
        dict: Success message.
    Raises:
        HTTPException: If operation fails.
    """
    try:
        # This would typically interact with SQL to mark the active branch
        return {"msg": f"Branch {data.branch_id} set as active for chat {data.chat_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set active branch: {str(e)}")