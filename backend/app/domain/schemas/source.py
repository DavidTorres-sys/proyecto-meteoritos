from pydantic import BaseModel
from typing import Optional

class SourceBase(BaseModel):
    net: Optional[str]
    locationSource: Optional[str]
    magSource: Optional[str]

class SourceCreate(SourceBase):
    pass

class SourceUpdate(SourceBase):
    pass

class SourceResponse(SourceBase):
    id: int
    earthquake_id: int

    class Config:
        orm_mode = True
