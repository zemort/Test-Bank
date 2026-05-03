import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request_credit import CreateUserRequestCredit
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.repay_account_fixture_model import RepayAccountFixtureModel
from src.main.api.models.repay_user_request import RepayUserRequest
from src.main.api.generators.number_generator import RandomNumberGenerator

@pytest.fixture
def user_repay_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequestCredit)

    api_manager.admin_steps.create_user_credit(user_request)

    account_response = api_manager.user_steps.create_account(user_request)

    credit_request = CreditUserRequest(
        accountId=account_response.id,
        amount=RandomNumberGenerator.generate_amount_credit(),
        termMonths=RandomNumberGenerator.generate_term_months()
    )

    credit_response = api_manager.user_steps.credit_user_valid(
        credit_request,
        user_request
    )

    repay_request = RepayUserRequest(
        creditId=credit_response.creditId,
        accountId=account_response.id,
        amount=credit_request.amount
    )

    return RepayAccountFixtureModel(
        user=user_request,
        account=account_response,
        credit_request=credit_request,
        credit=credit_response,
        repay_request=repay_request
    )