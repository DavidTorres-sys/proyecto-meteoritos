from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Meteorite(Base):
    __tablename__ = "meteorite"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    nametype = Column(String)
    mass = Column(Float)
    year = Column(Integer)

    fall_id = Column(Integer, ForeignKey("fall.id"))
    fall = relationship("Fall", back_populates="meteorite")
    
    reclass_id = Column(Integer, ForeignKey("reclass.id"))
    reclass = relationship("Reclass", back_populates="meteorite")

    geolocation_id = Column(Integer, ForeignKey("geolocation.id"))
    geolocation = relationship("Geolocation", back_populates="meteorite")