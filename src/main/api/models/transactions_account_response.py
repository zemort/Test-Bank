from src.main.api.models.base_model import BaseModel

class Transactions(BaseModel):
    transactionId: int
    type: str
    amount: float
    fromAccountId: int
    toAccountId: int
    createdAt: str

class TransactionsAccountRequest(BaseModel):
    id: int
    number: str
    balance: float
    transactions: Transactions
