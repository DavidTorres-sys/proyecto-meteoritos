from pydantic import BaseModel
from typing import Optional

class LocationBase(BaseModel):
    latitude: Optional[float] 
    longitude: Optional[float]

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationResponse(LocationBase):
    id: int
    earthquake_id: int

    class Config:
        orm_mode = True