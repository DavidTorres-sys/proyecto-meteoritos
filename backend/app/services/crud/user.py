from sqlalchemy.orm import Session
from .user_crud import *


def get_user(db: Session, user_id: int):
    return user_crud.read(db, user_id)

def create_user(db: Session, user):
    return user_crud.create(db, user)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return user_crud.read_all(db, skip=skip, limit=limit)

def get_user_by_email(db: Session, email: str):
    return user_crud.read_by_email(db, email)

def update_user(db: Session, user_id: int, user):
    return user_crud.update(db, user_id, user)


