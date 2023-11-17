from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Geolocation(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    reclat = Column(Float)
    reclong = Column(Float)

    meteorite_id = Column(Integer, ForeignKey("meteorite.id"))
    meteorite = relationship("Meteorite", back_populates="geolocation")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="geolocation")
