from pydantic import BaseModel
from typing import Optional

class StatusBase(BaseModel):
    status: Optional[str]

class StatusCreate(StatusBase):
    pass

class StatusUpdate(StatusBase):
    pass

class StatusResponse(StatusBase):
    id: int
    earthquake_id: int
    class Config:
        orm_mode = True