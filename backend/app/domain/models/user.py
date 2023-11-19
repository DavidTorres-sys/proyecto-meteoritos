from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
	__tablename__ = "user"
	
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String)
	last_name = Column(String)
	email = Column(String, unique=True)
	password = Column(String)
	
	form = relationship("Form", back_populates="user")
	location_users = relationship("LocationUser", back_populates="user")
