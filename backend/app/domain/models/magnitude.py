from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class Magnitude(Base):
    __tablename__ = "magnitude"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    mag = Column(Float)
    magType = Column(String)
    magError = Column(Float, nullable=True)
    magNst = Column(Float, nullable=True)
    
    earthquake_id = Column(Integer, ForeignKey('earthquake.id'))
    earthquake = relationship("Earthquake", back_populates="magnitude")