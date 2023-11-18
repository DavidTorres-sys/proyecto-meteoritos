from pydantic import BaseModel
from typing import Optional

class ReclassBase(BaseModel):
    name: str

class ReclassCreate(ReclassBase):
    meteorite_id: Optional[int] = None

class Reclass(ReclassBase):
    id: int
    meteorite_id: Optional[int] = None

    class Config:
        orm_mode = True
