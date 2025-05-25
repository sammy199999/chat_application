from sqlalchemy.orm import Session
from app.models.postgres_models import Chat
from app.schemas.chat import ChatCreate
import datetime

def create_chat(db: Session, chat: ChatCreate):
    """
    Create a new chat in the database.
    Args:
        db (Session): SQLAlchemy database session.
        chat (ChatCreate): Chat creation schema.
    Returns:
        Chat: The created chat object.
    Raises:
        Exception: If the database operation fails.
    """
    try:
        db_chat = Chat(**chat.dict())
        db.add(db_chat)
        db.commit()
        db.refresh(db_chat)
        return db_chat
    except Exception as e:
        db.rollback()
        raise Exception(f"Error creating chat: {str(e)}")

def get_chat(db: Session, chat_id):
    """
    Retrieve a chat by its ID.
    Args:
        db (Session): SQLAlchemy database session.
        chat_id: The ID of the chat to retrieve.
    Returns:
        Chat or None: The chat object if found, else None.
    Raises:
        Exception: If the database operation fails.
    """
    try:
        return db.query(Chat).filter(Chat.chat_id == chat_id).first()
    except Exception as e:
        raise Exception(f"Error retrieving chat: {str(e)}")

def update_chat(db: Session, chat_id, new_name: str):
    """
    Update the name of an existing chat.
    Args:
        db (Session): SQLAlchemy database session.
        chat_id: The ID of the chat to update.
        new_name (str): The new name for the chat.
    Returns:
        Chat or None: The updated chat object if found, else None.
    Raises:
        Exception: If the database operation fails.
    """
    try:
        db_chat = get_chat(db, chat_id)
        if db_chat:
            db_chat.name = new_name
            db_chat.updated_at = datetime.datetime.utcnow()
            db.commit()
            db.refresh(db_chat)
        return db_chat
    except Exception as e:
        db.rollback()
        raise Exception(f"Error updating chat: {str(e)}")

def delete_chat(db: Session, chat_id):
    """
    Delete a chat by its ID.
    Args:
        db (Session): SQLAlchemy database session.
        chat_id: The ID of the chat to delete.
    Raises:
        Exception: If the database operation fails.
    """
    try:
        db_chat = get_chat(db, chat_id)
        if db_chat:
            db.delete(db_chat)
            db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(f"Error deleting chat: {str(e)}")