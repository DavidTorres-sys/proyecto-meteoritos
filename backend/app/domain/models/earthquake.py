from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Earthquake(Base):
    __tablename__ = "earthquake"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    time = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

    location_earthquake = relationship("LocationEarthquake", back_populates="earthquake")
    magnitude = relationship("Magnitude", back_populates="earthquake")
    source = relationship("Source", back_populates="earthquake")
    status = relationship("Status", back_populates="earthquake")