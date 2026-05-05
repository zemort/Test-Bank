import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.deposit_account_fixture_model import DepositAccountFixtureModel



@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account_valid(self,
                                   api_manager: ApiManager,
                                   user_account_deposit: DepositAccountFixtureModel):

        deposit_response = api_manager.user_steps.deposit_account(
            user_account_deposit.deposit_request,
            user_account_deposit.user
        )

        assert deposit_response.balance == user_account_deposit.deposit_request.amount


    def test_deposit_account_invalid(self,
                                     api_manager,
                                     user_account_deposit: DepositAccountFixtureModel):

        user_account_deposit.deposit_request.amount = 500

        api_manager.user_steps.deposit_account_invalid(
            user_account_deposit.deposit_request,
            user_account_deposit.user
        )