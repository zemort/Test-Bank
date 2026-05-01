from http import HTTPStatus

import pytest

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_user_requester import CreateUserRequester
from src.main.api.requests.deposit_account_requester import DepositAccountRequester
from src.main.api.specs.requests_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs



@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self, api_manager):
        create_user_request = CreateUserRequest(
            username="Max160x",
            password="Pas!sw0rd",
            role="ROLE_USER"
        )

        api_manager.admin_steps.create_user(create_user_request)
        response_account_create = api_manager.user_steps.create_account(create_user_request)
        deposit_request = DepositAccountRequest(
            accountId=response_account_create.id,
            amount=1000
        )
        deposit_response = api_manager.user_steps.deposit_account(
            deposit_request,
            create_user_request
        )

        assert deposit_response.balance == deposit_request.amount


    def test_deposit_account_invalid(self, api_manager):
        create_user_request = CreateUserRequest(
            username="Max162x",
            password="Pas!sw0rd",
            role="ROLE_USER"
        )

        api_manager.admin_steps.create_user(create_user_request)
        response_account_create = api_manager.user_steps.create_account(create_user_request)
        deposit_request = DepositAccountRequest(
            accountId=response_account_create.id,
            amount=10
        )
        api_manager.user_steps.deposit_account_invalid(
            deposit_request,
            create_user_request
        )