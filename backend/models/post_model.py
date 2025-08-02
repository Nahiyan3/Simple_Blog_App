from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    author_id: str

class PostResponse(PostCreate):
    id: str
    created_at: datetime

class PostOut(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    author_name: str