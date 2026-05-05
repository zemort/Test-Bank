import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request_credit import CreateUserRequestCredit
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.credit_account_fixture_model import CreditAccountFixtureModel
from src.main.api.generators.number_generator import RandomNumberGenerator


@pytest.fixture
def user_credit_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequestCredit)

    api_manager.admin_steps.create_user_credit(user_request)

    account_response = api_manager.user_steps.create_account(user_request)

    credit_request = CreditUserRequest(
        accountId=account_response.id,
        amount=RandomNumberGenerator.generate_amount_credit(),
        termMonths=RandomNumberGenerator.generate_term_months()
    )

    return CreditAccountFixtureModel(
        user=user_request,
        account=account_response,
        credit_request=credit_request
    )