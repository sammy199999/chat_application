from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chat import ChatCreate, ChatOut, ChatUpdate
from app.crud.chat import create_chat, get_chat, update_chat, delete_chat
from app.db.session import get_db

router = APIRouter()

@router.post("/create-chat", response_model=ChatOut)
def create_chat_view(chat: ChatCreate, db: Session = Depends(get_db)):
    return create_chat(db, chat)

@router.get("/get-chat", response_model=ChatOut)
def get_chat_view(chat_id: str, db: Session = Depends(get_db)):
    chat = get_chat(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat

@router.put("/update-chat")
def update_chat_view(chat_id: str, chat: ChatUpdate, db: Session = Depends(get_db)):
    return update_chat(db, chat_id, chat.name)

@router.delete("/delete-chat")
def delete_chat_view(chat_id: str, db: Session = Depends(get_db)):
    delete_chat(db, chat_id)
    return {"msg": "Chat deleted"}