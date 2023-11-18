from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Reclass(Base):
    __tablename__ = "reclass"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    meteorite_id = Column(Integer, ForeignKey("meteorite.id"))
    meteorite = relationship("Meteorite", back_populates="reclass")
