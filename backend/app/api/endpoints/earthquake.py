from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.domain.schemas import *
from app.services.crud.earthquake import *

from typing import List

router = APIRouter()


@router.get("/earthquake/{earthquake_id}", response_model=EarthquakeResponse)
async def get_earthquake_(earthquake_id: int, db: Session = Depends(get_db)):
    try:
        db_earthquake = get_earthquake(db, earthquake_id)
        if db_earthquake is None:
            raise HTTPException(status_code=404, detail="Earthquake not found")

    except Exception as e:
        raise HTTPException(status_code=404, detail="Earthquake not found")
    return db_earthquake


@router.get("/earthquakes/", response_model=List[EarthquakeResponse])
async def get_earthquakes_(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        db_earthquakes = get_earthquakes(db, skip=skip, limit=limit)
        if db_earthquakes is None:
            raise HTTPException(
                status_code=404, detail="Earthquakes not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Earthquakes not found")
    return db_earthquakes

@router.get("/earthquakes/{latitud}/{longitud}/{radio_en_km}", response_model=List[EarthquakeResponse])
async def get_earthquakes_near(latitud: float, longitud: float, radio_en_km: float, db: Session = Depends(get_db)):
    try:
        db_earthquakes = await search_near_earthquakes(db, latitud, longitud, radio_en_km)
        if db_earthquakes is None:
            raise HTTPException(
                status_code=404, detail="Earthquakes not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Earthquakes not found")
    return db_earthquakes
