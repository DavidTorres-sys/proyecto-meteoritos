from app.services.crud.base import BASEcrud
from app.domain.models import Meteorite

class MeteoriteCrud(BASEcrud):
    def __init__(self, model=Meteorite):
        super().__init__(model)

meteorite_crud = MeteoriteCrud()
