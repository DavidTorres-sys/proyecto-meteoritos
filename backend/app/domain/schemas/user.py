from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str
    geolocation_id: Optional[int] = None

class User(UserBase):
    id: int
    geolocation_id: Optional[int] = None

    class Config:
        orm_mode = True
