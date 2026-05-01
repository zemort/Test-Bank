from src.main.api.models.base_model import BaseModel


class RepayUserRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float

