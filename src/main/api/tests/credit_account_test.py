import pytest

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_user_request import CreditUserRequest



@pytest.mark.api
class TestUserCredit:
    def test_user_credit(self, api_manager):
        create_user_request = CreateUserRequest(username="Max188c",
                                                password="Pas!sw0rd",
                                                role="ROLE_CREDIT_SECRET")

        api_manager.admin_steps.create_user(create_user_request)

        response_account_create = api_manager.user_steps.create_account(create_user_request)


        credit_user_request = CreditUserRequest(
            accountId=response_account_create.id,
            amount=5000,
            termMonths=12
        )

        credit_user_response = api_manager.user_steps.credit_user_valid(
            credit_user_request,
            create_user_request
        )

        assert credit_user_response.balance == credit_user_request.amount


    def test_user_credit_invalid(self, api_manager):
        create_user_request = CreateUserRequest(username="Max188c",
                                                password="Pas!sw0rd",
                                                role="ROLE_CREDIT_SECRET")

        api_manager.admin_steps.create_user(create_user_request)

        response_account_create = api_manager.user_steps.create_account(create_user_request)

        credit_user_request = CreditUserRequest(
            accountId=response_account_create.id,
            amount=4999,
            termMonths=12
        )

        api_manager.user_steps.credit_user_invalid(
            credit_user_request,
            create_user_request
        )