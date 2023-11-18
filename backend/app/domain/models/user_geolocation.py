from datetime import datetime
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base

class UserGeolocation(Base):
	__tablename__ = "user_geolocation"

	id = Column(Integer, primary_key=True, index=True)
	reclat = Column(Float)
	reclong = Column(Float)
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.datetime.utcnow)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship("User", back_populates="user_geolocation")