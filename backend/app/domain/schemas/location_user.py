from pydantic import BaseModel

class LocationUserBase(BaseModel):
    id: int
    location_id: int
    user_id: int

    class Config:
        orm_mode = True

class LocationUserCreate(LocationUserBase):
	location_id: int
	user_id: int
     
class LocationUserUpdate(LocationUserBase):
	pass

class LocationUserResponse(LocationUserBase):
	id: int
	location_id: int
	user_id: int

	class Config:
		orm_mode = True
    
