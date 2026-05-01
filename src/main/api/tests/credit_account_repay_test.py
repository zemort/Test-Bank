import pytest

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.repay_user_request import RepayUserRequest


@pytest.mark.api
class TestUserRepay:
    def test_user_repay_valid(self, api_manager):
        create_user_request = CreateUserRequest(username="Max156k",
                                                password="Pas!sw0rd",
                                                role="ROLE_CREDIT_SECRET"
                                                )
        api_manager.admin_steps.create_user(create_user_request)

        response_account_create = api_manager.user_steps.create_account(create_user_request)

        credit_user_request = CreditUserRequest(accountId=response_account_create.id,
                                                amount=5000,
                                                termMonths=12
                                                )

        credit_user_response = api_manager.user_steps.credit_user_valid(
            credit_user_request,
            create_user_request
        )

        deposit_request = DepositAccountRequest(
            accountId=response_account_create.id,
            amount=1000
        )

        deposit_response = api_manager.user_steps.deposit_account(
            deposit_request,
            create_user_request
        )

        repay_user_request = RepayUserRequest(creditId=credit_user_response.creditId,
                                              accountId=deposit_response.id, amount=5000)

        repay_user_response = api_manager.user_steps.credit_user_repay(
            repay_user_request,
            create_user_request
        )


        assert repay_user_response.amountDeposited == repay_user_request.amount
        assert repay_user_response.creditId == credit_user_response.creditId

    def test_user_repay_invalid(self, api_manager):
        create_user_request = CreateUserRequest(username="Max165ks",
                                                password="Pas!sw0rd",
                                                role="ROLE_CREDIT_SECRET"
                                                )
        api_manager.admin_steps.create_user(create_user_request)

        response_account_create = api_manager.user_steps.create_account(create_user_request)

        credit_user_request = CreditUserRequest(accountId=response_account_create.id,
                                                amount=5000,
                                                termMonths=12
                                                )

        credit_user_response = api_manager.user_steps.credit_user_valid(
            credit_user_request,
            create_user_request
        )

        deposit_request = DepositAccountRequest(
            accountId=response_account_create.id,
            amount=1000
        )

        deposit_response = api_manager.user_steps.deposit_account(
            deposit_request,
            create_user_request
        )

        repay_user_request = RepayUserRequest(creditId=credit_user_response.creditId,
                                              accountId=deposit_response.id, amount=10)

        api_manager.user_steps.credit_user_repay_invalid(
            repay_user_request,
            create_user_request
        )