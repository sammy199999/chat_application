from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.chat import ChatCreate, ChatOut, ChatUpdate
from app.crud.chat import create_chat, get_chat, update_chat, delete_chat
from app.db.session import get_db
from app.auth.auth import get_api_key


router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post("/create-chat", response_model=ChatOut)
def create_chat_view(chat: ChatCreate, db: Session = Depends(get_db)):
    """
    Create a new chat.
    Args:
        chat (ChatCreate): Chat creation data.
        db (Session): Database session dependency.
    Returns:
        ChatOut: Created chat object.
    Raises:
        HTTPException: If chat creation fails.
    """
    try:
        return create_chat(db, chat)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create chat: {str(e)}")

@router.get("/get-chat", response_model=ChatOut)
def get_chat_view(chat_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a chat by its ID.
    Args:
        chat_id (str): ID of the chat to retrieve.
        db (Session): Database session dependency.
    Returns:
        ChatOut: Retrieved chat object.
    Raises:
        HTTPException: If chat is not found or retrieval fails.
    """
    try:
        chat = get_chat(db, chat_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")
        return chat
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get chat: {str(e)}")

@router.put("/update-chat")
def update_chat_view(chat_id: str, chat: ChatUpdate, db: Session = Depends(get_db)):
    """
    Update an existing chat's name.
    Args:
        chat_id (str): ID of the chat to update.
        chat (ChatUpdate): Updated chat data.
        db (Session): Database session dependency.
    Returns:
        dict: Result of the update operation.
    Raises:
        HTTPException: If update fails.
    """
    try:
        return update_chat(db, chat_id, chat.name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update chat: {str(e)}")

@router.delete("/delete-chat")
def delete_chat_view(chat_id: str, db: Session = Depends(get_db)):
    """
    Delete a chat by its ID.
    Args:
        chat_id (str): ID of the chat to delete.
        db (Session): Database session dependency.
    Returns:
        dict: Success message.
    Raises:
        HTTPException: If deletion fails.
    """
    try:
        delete_chat(db, chat_id)
        return {"msg": "Chat deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete chat: {str(e)}")