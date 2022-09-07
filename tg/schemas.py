from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Chat(BaseModel):
    id: int
    # is_bot: bool
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]


class User(Chat):
    is_admin: bool = False


class UserDB(User):
    key: str
    parent_ref: Optional[str] = ""

class Entity(BaseModel):
    offset: int
    length: int
    type: str


class Message(BaseModel):
    message_id: int
    chat: Chat
    date: int
    text: Optional[str]
    entities: Optional[List[Entity]]

class Update(BaseModel):
    message: Optional[Message]
