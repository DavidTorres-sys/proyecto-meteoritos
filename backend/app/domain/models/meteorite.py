from sqlalchemy import Column, Integer, String, Float

from app.db.database import Base


class Meteorite(Base):
    __tablename__ = "meteorite"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    idMeteorite = Column(Integer)
    nametype = Column(String)
    recclass = Column(String)
    mass = Column(Float)
    fall = Column(String)
    year = Column(Integer)
    reclat = Column(Float)
    reclong = Column(Float)
    geolocation = Column(String)

