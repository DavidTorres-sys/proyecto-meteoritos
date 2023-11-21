from pydantic import BaseModel
from app.domain.schemas.location_user import *
class UserBase(BaseModel):
    name: str
    last_name: str
    email: str

class UserUpdate(UserBase):
    pass

class UserCreate(UserBase):
    password: str
    location_user: LocationUserCreate
class UserResponse(UserBase):
    id: int
    location_user: LocationUserResponse


    class Config:
        orm_mode = True
