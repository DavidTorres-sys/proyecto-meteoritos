from pydantic import BaseModel
from typing import Optional

class GeolocationBase(BaseModel):
    reclat: float
    reclong: float

class GeolocationCreate(GeolocationBase):
    meteorite_id: Optional[int] = None
    user_id: Optional[int] = None

class Geolocation(GeolocationBase):
    id: int
    meteorite_id: Optional[int] = None
    user_id: Optional[int] = None

    class Config:
        orm_mode = True
