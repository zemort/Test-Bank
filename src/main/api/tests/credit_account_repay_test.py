import pytest

from src.main.api.models.repay_account_fixture_model import RepayAccountFixtureModel


@pytest.mark.api
class TestUserRepay:
    def test_user_repay_valid(self,
                              api_manager,
                              user_repay_request: RepayAccountFixtureModel):

        repay_response = api_manager.user_steps.credit_user_repay(
            user_repay_request.repay_request,
            user_repay_request.user
        )


        assert repay_response.amountDeposited == user_repay_request.credit_request.amount
        assert repay_response.creditId == user_repay_request.credit.creditId

    def test_user_repay_invalid(self,
                                api_manager,
                                user_repay_request: RepayAccountFixtureModel):
        user_repay_request.repay_request.amount = 100

        api_manager.user_steps.credit_user_repay_invalid(
            user_repay_request.repay_request,
            user_repay_request.user
        )