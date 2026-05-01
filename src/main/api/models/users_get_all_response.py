from src.main.api.models.base_model import BaseModel


class UsersGetAllResponse(BaseModel):
    id: int
    username: str
    role: str