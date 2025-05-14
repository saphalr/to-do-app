from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class ToDoRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
