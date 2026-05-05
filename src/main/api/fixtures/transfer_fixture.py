import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.transfer_account_fixture_model import TransferAccountFixtureModel
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.generators.number_generator import RandomNumberGenerator

@pytest.fixture
def user_transfer_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)

    api_manager.admin_steps.create_user(user_request)

    account_response_1 = api_manager.user_steps.create_account(user_request)
    account_response_2 = api_manager.user_steps.create_account(user_request)

    deposit_request = DepositAccountRequest(
        accountId= account_response_1.id,
        amount=RandomNumberGenerator.generate_amount_deposit()
    )

    deposit_response = api_manager.user_steps.deposit_account(
        deposit_request,
        user_request
    )


    transfer_request = TransferAccountRequest(
        fromAccountId=account_response_1.id,
        toAccountId=account_response_2.id,
        amount=deposit_request.amount
    )

    return TransferAccountFixtureModel(
        user=user_request,
        account_1=account_response_1,
        account_2=account_response_2,
        deposit_account_request=deposit_request,
        deposit_account_response=deposit_response,
        transfer_account_request=transfer_request
    )