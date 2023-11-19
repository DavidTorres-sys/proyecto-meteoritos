from typing import Optional
from pydantic import BaseModel

class MagnitudeBase(BaseModel):
    mag: Optional[float]
    magType: Optional[str]
    nst: Optional[int]
    gap: Optional[float]
    dmin: Optional[float]
    rms: Optional[float]
    horizontalError: Optional[float]
    depthError: Optional[float]
    magError: Optional[float]
    magNst: Optional[int]

class MagnitudeCreate(MagnitudeBase):
    pass

class MagnitudeUpdate(MagnitudeBase):
    pass

class MagnitudeResponse(MagnitudeBase):
    id: int
    earthquake_id: int

    class Config:
        orm_mode = True