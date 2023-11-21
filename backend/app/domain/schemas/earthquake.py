from datetime import datetime
from pydantic import BaseModel
from app.domain.schemas import *
from app.domain.schemas.location_earthquake import *

class EarthquakeBase(BaseModel):
    time: datetime
    updated: datetime

class EarthquakeCreate(EarthquakeBase):
    location: LocationEarthquakeCreate
    magnitude: MagnitudeCreate
    source: SourceCreate
    status: StatusCreate

class EarthquakeUpdate(EarthquakeBase):
    pass

class EarthquakeResponse(EarthquakeBase):
    id: int
    location: LocationEarthquakeResponse
    magnitude: MagnitudeResponse
    source: SourceResponse
    status: StatusResponse


    class Config:
        orm_mode = True
