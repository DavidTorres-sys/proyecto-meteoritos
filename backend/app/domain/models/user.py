from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String)
	last_name = Column(String)
	email = Column(String, unique=True)
	password = Column(String)

	geolocation_id = Column(Integer, ForeignKey("geolocation.id"))
	geolocation = relationship("Geolocation", back_populates="user")
