from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class LocationUser(Base):
    __tablename__ = "location_user"

    id = Column(Integer, primary_key=True, index=True)
    
    location_id = Column(Integer, ForeignKey("location.id"))
    location = relationship("Location", back_populates="location_users")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="location_users")