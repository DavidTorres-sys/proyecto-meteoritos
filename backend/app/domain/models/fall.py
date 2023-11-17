from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Fall(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String)
    
    meteorite_id = Column(Integer, ForeignKey("meteorite.id"))
    meteorite = relationship("Meteorite", back_populates="fall")
