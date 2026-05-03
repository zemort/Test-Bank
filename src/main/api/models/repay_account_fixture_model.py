from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_request_credit import CreateUserRequestCredit
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.credit_user_response import CreditUserResponse
from src.main.api.models.repay_user_request import RepayUserRequest


class RepayAccountFixtureModel(BaseModel):
    user: CreateUserRequestCredit
    account: CreateAccountResponse
    credit_request: CreditUserRequest
    credit: CreditUserResponse
    repay_request: RepayUserRequest