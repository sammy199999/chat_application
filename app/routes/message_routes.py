from fastapi import APIRouter, Depends
from app.schemas.message import MessageCreate
from app.db.mongo import get_mongo_client
from app.crud.message import add_message, get_chat_history

router = APIRouter()

@router.post("/add-message")
async def add_message_view(message: MessageCreate, mongo_client=Depends(get_mongo_client)):
    await add_message(mongo_client, message.dict())
    return {"msg": "Message added"}

@router.get("/get-messages")
async def get_messages_view(chat_id: str, mongo_client=Depends(get_mongo_client)):
    return await get_chat_history(mongo_client, chat_id)