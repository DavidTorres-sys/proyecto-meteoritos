from app.services.crud.base import BASEcrud
from app.domain.models import LocationUser

class LocationUserCrud(BASEcrud):
    def __init__(self, model = LocationUser):
        super().__init__(model)
        
location_user_crud = LocationUserCrud()