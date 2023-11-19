from app.db.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)
    
    earthquake_id = Column(Integer, ForeignKey('earthquake.id'))
    earthquake = relationship("Earthquake", back_populates="location")

    location_users = relationship("LocationUser", back_populates="location")