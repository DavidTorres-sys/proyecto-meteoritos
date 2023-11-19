from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy.ext.asyncio import AsyncSession


class BASEcrud:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, obj_in):
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def read(self, db: Session, obj_id):
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def update(self, db: Session, obj_id, obj_in):
        db_obj = db.query(self.model).filter(self.model.id == obj_id).first()
        for field, value in obj_in.dict().items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, obj_id):
        db_obj = db.query(self.model).filter(self.model.id == obj_id).first()
        db.delete(db_obj)
        db.commit()
        return db_obj

    def read_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()
