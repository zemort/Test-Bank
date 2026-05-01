from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_request import CreateAccountRequest
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.credit_user_response import CreditUserResponse
from src.main.api.models.delete_users_response import DeleteUserResponse
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.deposit_account_response import DepositAccountResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.repay_user_response import RepayUserResponse
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.models.transfer_account_response import TransferAccountResponse


@dataclass
class EndpointConfigConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]



class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfigConfiguration(
        request_model = CreateUserRequest,
        url = "/admin/create",
        response_model = CreateUserResponse
    )

    ADMIN_DELETE_USER = EndpointConfigConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = DeleteUserResponse
    )

    LOGIN_USER = EndpointConfigConfiguration(
        request_model= LoginUserRequest,
        url= "/auth/token/login",
        response_model= LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfigConfiguration(
        request_model= CreateAccountRequest,
        url="/account/create",
        response_model=CreateAccountResponse
    )

    DEPOSIT_ACCOUNT = EndpointConfigConfiguration(
        request_model= DepositAccountRequest,
        url="/account/deposit",
        response_model=DepositAccountResponse
    )

    TRANSFER_ACCOUNT = EndpointConfigConfiguration(
        request_model= TransferAccountRequest,
        url="/account/transfer",
        response_model=TransferAccountResponse
    )

    CREDIT_USER = EndpointConfigConfiguration(
        request_model= CreditUserRequest,
        url="/credit/request",
        response_model=CreditUserResponse
    )

    REPAY_CREDIT = EndpointConfigConfiguration(
        request_model= RepayUserResponse,
        url="/credit/repay",
        response_model=RepayUserResponse
    )