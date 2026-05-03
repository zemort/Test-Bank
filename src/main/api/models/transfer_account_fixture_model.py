from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest


class TransferAccountFixtureModel(BaseModel):
    user: CreateUserRequest
    account_1: CreateAccountResponse
    account_2: CreateAccountResponse
    deposit_account_request: DepositAccountRequest
    deposit_account_response: DepositAccountResponse
    transfer_account_request: TransferAccountRequest