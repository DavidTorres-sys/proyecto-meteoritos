from .location_user_crud import *
from sqlalchemy.orm import Session
from app.domain.schemas import LocationUserCreate


def create_location_user(db: Session, location_user: LocationUserCreate):
    return location_user_crud.create(db, obj_in=location_user)
