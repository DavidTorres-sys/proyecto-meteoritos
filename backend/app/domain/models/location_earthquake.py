from app.db.database import Base
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class LocationEarthquake(Base):
    __tablename__ = "location_earthquake"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))
    
    earthquake_id = Column(Integer, ForeignKey('earthquake.id'))
    earthquake = relationship("Earthquake", back_populates="location_earthquake")