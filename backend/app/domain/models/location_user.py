from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from app.db.database import Base

class LocationUser(Base):
    __tablename__ = "location_user"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="location_user")