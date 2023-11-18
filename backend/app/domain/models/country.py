from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Country(Base):
  __tablename__ = "country"
  
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  name = Column(String, unique=True)
  
  meteorite_geolocation = relationship("MeteoriteGeolocation", back_populates="country")
  user_geolocation = relationship("UserGeolocation", back_populates="country")