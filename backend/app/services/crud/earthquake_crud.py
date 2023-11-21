from app.services.crud.base import BASEcrud
from app.domain.models import Earthquake

class EarthquakeCrud(BASEcrud):
    def __init__(self, model = Earthquake):
        super().__init__(model)

earthquake_crud = EarthquakeCrud()
