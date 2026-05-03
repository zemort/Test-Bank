import pytest

from src.main.api.models.credit_account_fixture_model import CreditAccountFixtureModel



@pytest.mark.api
class TestUserCredit:
    def test_user_credit(self,
                         api_manager,
                         user_credit_request: CreditAccountFixtureModel):

        credit_response = api_manager.user_steps.credit_user_valid(
            user_credit_request.credit_request,
            user_credit_request.user
        )

        assert credit_response.balance == user_credit_request.credit_request.amount


    def test_user_credit_invalid(self,
                                 api_manager,
                                 user_credit_request: CreditAccountFixtureModel):
        user_credit_request.credit_request.amount = 1000

        api_manager.user_steps.credit_user_invalid(
            user_credit_request.credit_request,
            user_credit_request.user
        )