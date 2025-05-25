from fastapi import APIRouter, Depends, HTTPException
from app.schemas.message import MessageCreate
from app.db.mongo import get_mongo_client
from app.crud.message import add_message, get_chat_history
from app.auth.auth import get_api_key


router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post("/add-message")
async def add_message_view(message: MessageCreate, mongo_client=Depends(get_mongo_client)):
    """
    Add a new message to a chat.
    Args:
        message (MessageCreate): Message creation data.
        mongo_client: MongoDB client dependency.
    Returns:
        dict: Success message.
    Raises:
        HTTPException: If message addition fails.
    """
    try:
        await add_message(mongo_client, message.dict())
        return {"msg": "Message added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add message: {str(e)}")

@router.get("/get-messages")
async def get_messages_view(chat_id: str, mongo_client=Depends(get_mongo_client)):
    """
    Retrieve all messages for a given chat.
    Args:
        chat_id (str): ID of the chat to retrieve messages for.
        mongo_client: MongoDB client dependency.
    Returns:
        list: List of messages for the chat.
    Raises:
        HTTPException: If retrieval fails.
    """
    try:
        return await get_chat_history(mongo_client, chat_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get messages: {str(e)}")