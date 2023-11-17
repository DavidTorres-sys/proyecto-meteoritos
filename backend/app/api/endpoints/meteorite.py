from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from app.domain.models import Meteorite
from app.services.crud.meteorite_service import *
from app.utils.database import get_db
# from shapely.geometry import Point

from typing import List

router = APIRouter()

@router.get("/meteorites/{meteorite_id}")
def read_meteorite(meteorite_id: int, db: Session = Depends(get_db)) -> Meteorite:
    try:
        meteorite = get_meteorite(db, meteorite_id)
        if meteorite is None:
            raise HTTPException(status_code=404, detail="Meteorite not found")
    except:
        raise HTTPException(status_code=500, detail="Server error")
    return meteorite


@router.get("/meteorites")
def read_meteorites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Meteorite]:
    try:
        meteorites = get_meteorites(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=500, detail="Server error")
    return meteorites


@router.get("/mass_distribution")
async def get_mass_distribution(db: Session = Depends(get_db)):
    try:
        df = get_characteristics()
        mass_distribution = analyze_mass_distribution(df)
        return {"mass_distribution": mass_distribution}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/class_distribution")
async def get_class_distribution(db: Session = Depends(get_db)):
    try:
        df = get_characteristics()
        class_distribution = analyze_class_distribution(df)
        return {"class_distribution": class_distribution}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/location_distribution")
async def get_location_distribution(db: Session = Depends(get_db)):
    try:
        df = get_characteristics()
        location_distribution = analyze_location_distribution(df)
        return {"location_distribution": location_distribution}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.get("/class")
async def get_class(db: Session = Depends(get_db)):
    try:
        df = get_characteristics()
        recclass = analyze_class(df)
        return {"class": recclass}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@router.get("/meteorites/continent/{meteorite_id}")
async def get_continent(meteorite_id: int, db: Session = Depends(get_db)):
    try:
        continent = get_continent_from_coordinates(meteorite_id)
        return {"continent": continent}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)