from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Magnitude(Base):
    __tablename__ = "magnitude"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    mag = Column(Float)
    magType = Column(String)
    nst = Column(Integer, nullable=True)
    gap = Column(Float, nullable=True)
    dmin = Column(Float, nullable=True)
    rms = Column(Float, nullable=True)
    horizontalError = Column(Float, nullable=True)
    depthError = Column(Float, nullable=True)
    magError = Column(Float, nullable=True)
    magNst = Column(Integer, nullable=True)
    
    earthquake_id = Column(Integer, ForeignKey('earthquake.id'))
    earthquake = relationship("Earthquake", back_populates="magnitude")