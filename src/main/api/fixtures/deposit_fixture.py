import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_fixture_model import DepositAccountFixtureModel
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.generators.number_generator import RandomNumberGenerator


@pytest.fixture
def user_account_deposit(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)

    api_manager.admin_steps.create_user(user_request)

    account_response = api_manager.user_steps.create_account(user_request)

    deposit_request = DepositAccountRequest(
        accountId=account_response.id,
        amount=RandomNumberGenerator.generate_amount_deposit()
    )

    return DepositAccountFixtureModel(
        user=user_request,
        account=account_response,
        deposit_request=deposit_request
    )