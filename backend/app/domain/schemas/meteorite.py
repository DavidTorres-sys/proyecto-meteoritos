from pydantic import BaseModel

class Meteorite(BaseModel):
    name: str
    id: int
    nametype: str
    recclass: str
    mass: int
    fall: str
    year: int
    reclat: float
    reclong: float
    geolocation: str

    class Config:
        orm_mode = True