from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String)

    earthquake_id = Column(Integer, ForeignKey('earthquake.id'))
    earthquake = relationship("Earthquake", back_populates="status")
