from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Form(Base):
    __tablename__ = "form"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    housing_type = Column(String)
    emergency_resources = Column(Boolean)
    evacuation_plan = Column(Boolean)
    experience_emergency = Column(Boolean)
    medical_conditions = Column(Boolean)
    participation_drills = Column(Boolean)
    comunication_device = Column(Boolean)
    result = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="form")
