from pydantic import BaseModel
from typing import Optional

class FallBase(BaseModel):
    type: str

class FallCreate(FallBase):
    meteorite_id: Optional[int] = None

class Fall(FallBase):
    id: int
    meteorite_id: Optional[int] = None

    class Config:
        orm_mode = True
