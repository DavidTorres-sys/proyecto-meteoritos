from typing import Optional
from pydantic import BaseModel

class MeteoriteBase(BaseModel):
    name: str
    nametype: str
    mass: float
    year: int

class MeteoriteCreate(MeteoriteBase):
    fall_id: Optional[int] = None
    reclass_id: Optional[int] = None
    geolocation_id: Optional[int] = None

class Meteorite(MeteoriteBase):
    id: int
    fall_id: Optional[int] = None
    reclass_id: Optional[int] = None
    geolocation_id: Optional[int] = None

    class Config:
        orm_mode = True
