from typing import Optional
from pydantic import BaseModel

class FormBase(BaseModel):
    housing_type: str
    emergency_resources: bool
    evacuation_plan: bool
    experience_emergency: bool
    medical_conditions: bool
    participation_drills: bool
    comunication_device: bool
    result: Optional[str] = None

class FormCreate(FormBase):
    user_id: Optional[int] = None

class FormUpdate(FormBase):
    pass

class FormResponse(FormBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
