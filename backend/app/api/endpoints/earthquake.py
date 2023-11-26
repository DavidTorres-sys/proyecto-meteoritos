from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.utils.database import get_db
from app.domain.schemas import *
from app.services.crud.earthquake import *
from app.services.crud.charts import *


from typing import List

router = APIRouter()


@router.get("/earthquakes/{earthquake_id}", response_model=EarthquakeResponse)
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


@router.post("/earthquakes/calculate_earthquake_probability/{user_latitude}/{user_longitude}")
async def calculate_earthquake_endpoint(
    model_answers: FormCreate,
    user_latitude: float,
    user_longitude: float,
    db: Session = Depends(get_db)
):
    try:
        db_earthquakes = get_earthquake_data(
            db, user_latitude, user_longitude, 200)
        average_magnitude = calculate_average_magnitude(db_earthquakes)
        earthquake_probability = calculate_probability(model_answers)
        suggestions = generate_specific_suggestions(model_answers)

        return {"suggested_actions": earthquake_probability, "average_magnitude": average_magnitude, "specific_suggestions": suggestions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/earthquakes/near/{limit}/{user_latitude}/{user_longitude}", response_model=List[EarthquakeResponse])
async def get_earthquakes_near_endpoint(
    user_latitude: float,
    user_longitude: float,
    limit: int,
    db: Session = Depends(get_db)
):
    try:
        print(f"User Latitude: {user_latitude}, User Longitude: {user_longitude}")
        db_earthquakes = get_earthquake_data(db, user_latitude, user_longitude, limit)
        if db_earthquakes is None:
            raise HTTPException(status_code=404, detail="Earthquakes not found")
        return db_earthquakes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/earthquakes/near/{limit}/{user_latitude}/{user_longitude}/probability")
async def analisys_data(
    user_latitude: float,
    user_longitude: float,
    limit: int,
    db: Session = Depends(get_db)
):
    try:
        db_earthquakes = get_earthquake_data(db, user_latitude, user_longitude, limit)
        response = analisys_earthquakes(db_earthquakes)
        # map_chart = BaiduMapChartBuilder() \
        # .set_title("Earthquakes", "", " ", "center") \
        # .set_tooltip("item") \
        # .set_bmap([user_latitude, user_longitude], 5, True, [
        #     {"featureType": "water", "elementType": "all", "stylers": {"color": "#d1d1d1"}},
        # ]) \
        # .add_scatter_series("pm2.5", response[:5], lambda val: val[2] / 10, 2, '{b}', 'right', False, True) \
        # .add_effect_scatter_series("Top 5", response[:5], lambda val: val[2] / 10, 2, 'render', 'stroke', '{b}', 'right', True, {"shadowBlur": 10, "shadowColor": "#333"}, True, 1) \
        # .build()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)
)
    

