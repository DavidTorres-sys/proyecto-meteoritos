from pydantic import BaseModel

class LocationEarthquakeBase(BaseModel):
    latitude: float
    longitude: float

class LocationEarthquakeCreate(LocationEarthquakeBase):
    pass

class LocationEarthquakeUpdate(LocationEarthquakeBase):
    pass

class LocationEarthquakeResponse(LocationEarthquakeBase):
    id: int
    earthquake_id: int

    class Config:
        orm_mode = True