import pytest

from src.main.api.fixtures.api_fixture import api_manager



@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account(self,
                              api_manager,
                              user_transfer_request):

        transfer_response = api_manager.user_steps.transfer_account(
            user_transfer_request.transfer_account_request,
            user_transfer_request.user
        )

        assert transfer_response.fromAccountIdBalance == user_transfer_request.deposit_account_request.amount - user_transfer_request.transfer_account_request.amount

    def test_transfer_account_invalid(self,
                                      api_manager,
                                      user_transfer_request):
        user_transfer_request.transfer_account_request.amount = 499

        api_manager.user_steps.transfer_account_invalid(
            user_transfer_request.transfer_account_request,
            user_transfer_request.user
        )

