from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import JSONResponse
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


@router.post("/calculate_earthquake_probability")
async def calculate_earthquake_endpoint(
    model_answers: FormCreate,
    user_latitude: float = Body(...),
    user_longitude: float = Body(...),
    db: Session = Depends(get_db)
):
    try:
        earthquake_probability_class = calculate_earthquake_probability(
            user_latitude, user_longitude, model_answers)
        return {"earthquake_probability_class": earthquake_probability_class}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/earthquake/near/", response_model=List[EarthquakeResponse])
async def get_earthquakes_near_endpoint(
    user_latitude: float,
    user_longitude: float,
    db: Session = Depends(get_db)
):
    try:
        print(f"User Latitude: {user_latitude}, User Longitude: {user_longitude}")
        db_earthquakes = get_earthquake_data(
            db, user_latitude, user_longitude)
        print(db_earthquakes)
        return db_earthquakes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
