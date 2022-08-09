from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
