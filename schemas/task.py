from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    id: Optional[str]
    user_id: str
    title: str
    description: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
