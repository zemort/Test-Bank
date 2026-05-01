from src.main.api.models.base_model import BaseModel


class RepayUserResponse(BaseModel):
    creditId: int
    amountDeposited: float