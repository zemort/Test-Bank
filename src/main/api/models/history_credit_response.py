from src.main.api.models.base_model import BaseModel

class Credits(BaseModel):
    creditId: int
    accountId: int
    amount: float
    termMonths: int
    balance: int
    createdAt: str

class HistoryCreditResponse(BaseModel):
    userId: int
    accountId: int
    amount: float
    credits: Credits

