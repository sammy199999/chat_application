from sqlalchemy import Column, String, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import enum
import uuid
import datetime

Base = declarative_base()

class ChatType(enum.Enum):
    personal = "personal"
    group = "group"

class Chat(Base):
    __tablename__ = 'chats'
    chat_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id = Column(String, nullable=False)
    chat_type = Column(Enum(ChatType), default=ChatType.personal)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    active = Column(Boolean, default=True)

class Conversation(Base):
    __tablename__ = 'conversations'
    chat_id = Column(UUID(as_uuid=True), ForeignKey('chats.chat_id'), primary_key=True)
    account_id = Column(String, nullable=False)
    name = Column(String)
    deleted = Column(Boolean, default=False)