from pydantic import BaseModel

class LocationUserBase(BaseModel):
    latitude: float
    longitude: float


class LocationUserCreate(LocationUserBase):
    pass


class LocationUserUpdate(LocationUserBase):
    pass


class LocationUserResponse(LocationUserBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
