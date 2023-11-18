from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Form(Base):
	__tablename__ = "form"
	
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	Housing_type = Column(String)
	Emergency_resources = Column(Boolean)
	Evacuation_plan = Column(Boolean)
	Experience_emergency = Column(Boolean)
	Medical_conditions = Column(Boolean)
	Participation_drills = Column(Boolean)
	comunication_device = Column(Boolean)
	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship("User", back_populates="form",)