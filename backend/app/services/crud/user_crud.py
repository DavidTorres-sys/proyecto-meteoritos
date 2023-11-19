from app.services.crud.base import BASEcrud
from app.domain.models import User

class UserCrud(BASEcrud):
    def __init__(self, model = User):
        super().__init__(model)

user_crud = UserCrud()