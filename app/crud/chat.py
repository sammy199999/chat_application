from sqlalchemy.orm import Session
from app.models.postgres_models import Chat
from app.schemas.chat import ChatCreate
import datetime

def create_chat(db: Session, chat: ChatCreate):
    db_chat = Chat(**chat.dict())
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def get_chat(db: Session, chat_id):
    return db.query(Chat).filter(Chat.chat_id == chat_id).first()

def update_chat(db: Session, chat_id, new_name: str):
    db_chat = get_chat(db, chat_id)
    if db_chat:
        db_chat.name = new_name
        db_chat.updated_at = datetime.datetime.utcnow()
        db.commit()
    return db_chat

def delete_chat(db: Session, chat_id):
    db_chat = get_chat(db, chat_id)
    if db_chat:
        db.delete(db_chat)
        db.commit()