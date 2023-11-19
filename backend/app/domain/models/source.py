from app.db.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    net = Column(String)
    locationSource = Column(String)
    magSource = Column(String)

    earthquake_id = Column(Integer, ForeignKey('earthquake.id'))
    earthquake = relationship("Earthquake", back_populates="source")