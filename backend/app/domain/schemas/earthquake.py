from datetime import datetime
from pydantic import BaseModel
from typing import List
from . import *

class EarthquakeBase(BaseModel):
    time: datetime
    updated: datetime

class EarthquakeCreate(EarthquakeBase):
    location: List[LocationCreate]
    magnitude: List[MagnitudeCreate]
    source: List[SourceCreate]
    status: List[StatusCreate]

class EarthquakeUpdate(EarthquakeBase):
    pass

class EarthquakeResponse(EarthquakeBase):
    id: int
    location: List[LocationResponse]
    magnitude: List[MagnitudeResponse]
    source: List[SourceResponse]
    status: List[StatusResponse]


    class Config:
        orm_mode = True
