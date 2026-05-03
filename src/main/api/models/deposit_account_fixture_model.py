from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest


class DepositAccountFixtureModel(BaseModel):
    user: CreateUserRequest
    account: CreateAccountResponse
    deposit_request: DepositAccountRequest