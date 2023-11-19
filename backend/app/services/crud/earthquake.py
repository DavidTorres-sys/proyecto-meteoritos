from sqlalchemy.orm import Session
from .earthquake_crud import *
from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession


def get_earthquake(db: Session, meteorite_id: int):
    return earthquake_crud.read(db, meteorite_id)


def get_earthquakes(db: Session, skip: int = 0, limit: int = 100):
    return earthquake_crud.read_all(db, skip=skip, limit=limit)

async def search_near_earthquakes(db: AsyncSession, latitude, longitude, radio_km=100):
    query = text(
        f"""
        SELECT e.*
        FROM earthquake e
        JOIN location l ON e.id = l.earthquake_id
        WHERE ST_DWithin(
            ST_MakePoint(:longitude, :latitude)::geography,
            ST_MakePoint(l.longitude, l.latitude)::geography,
            :radio_km * 1000
        )
        """
    )

    # Note: Use await and fetchall() to get the results
    result = await db.execute(query, {"latitude": latitude, "longitude": longitude, "radio_km": radio_km})
    near_earthquakes = [dict(row) for row in (await result.fetchall())]

    return near_earthquakes
