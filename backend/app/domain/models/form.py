from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Form(Base):
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)

	user_id = Column(Integer, ForeignKey("user.id"))
	user = relationship("User", back_populates="form")