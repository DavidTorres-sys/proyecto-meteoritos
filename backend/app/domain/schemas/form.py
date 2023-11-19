from typing import Optional
from pydantic import BaseModel

class FormBase(BaseModel):
    Housing_type: str
    Emergency_resources: bool
    Evacuation_plan: bool
    Experience_emergency: bool
    Medical_conditions: bool
    Participation_drills: bool
    comunication_device: bool

class FormCreate(FormBase):
    user_id: Optional[int] = None

class FormUpdate(FormBase):
    pass

class FormResponse(FormBase):
    id: int
    user_id: Optional[int] = None

    class Config:
        orm_mode = True
