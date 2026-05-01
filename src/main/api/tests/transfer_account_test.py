import pytest

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest



@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account(self, api_manager):
        create_user_request = CreateUserRequest(
            username="Max177x",
            password="Pas!sw0rd",
            role="ROLE_USER"
        )

        api_manager.admin_steps.create_user(create_user_request)

        response_account_create_1 = api_manager.user_steps.create_account(create_user_request)
        response_account_create_2 = api_manager.user_steps.create_account(create_user_request)
        deposit_request = DepositAccountRequest(
            accountId=response_account_create_1.id,
            amount=1000
        )
        deposit_response = api_manager.user_steps.deposit_account(
            deposit_request,
            create_user_request
        )

        deposit_account_value = deposit_response.balance

        transfer_account_request = TransferAccountRequest(fromAccountId=response_account_create_1.id,
                                                          toAccountId=response_account_create_2.id,
                                                          amount=500.75)
        transfer_response = api_manager.user_steps.transfer_account(
            transfer_account_request,
            create_user_request,
        )

        assert transfer_response.fromAccountIdBalance == deposit_account_value - transfer_account_request.amount

    def test_transfer_account_invalid(self, api_manager):
        create_user_request = CreateUserRequest(
            username="Max177x",
            password="Pas!sw0rd",
            role="ROLE_USER"
        )

        api_manager.admin_steps.create_user(create_user_request)

        response_account_create_1 = api_manager.user_steps.create_account(create_user_request)
        response_account_create_2 = api_manager.user_steps.create_account(create_user_request)
        deposit_request = DepositAccountRequest(
            accountId=response_account_create_1.id,
            amount=1000
        )
        deposit_response = api_manager.user_steps.deposit_account(
            deposit_request,
            create_user_request
        )

        transfer_account_request = TransferAccountRequest(fromAccountId=response_account_create_1.id,
                                                          toAccountId=response_account_create_2.id,
                                                          amount=499.75)
        api_manager.user_steps.transfer_account_invalid(
            transfer_account_request,
            create_user_request,
        )