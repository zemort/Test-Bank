from src.main.api.fixtures.user_fixture import create_user_request
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_user_request import CreditUserRequest
from src.main.api.models.deposit_account_request import DepositAccountRequest
from src.main.api.models.repay_user_request import RepayUserRequest
from src.main.api.models.transfer_account_request import TransferAccountRequest
from src.main.api.specs.requests_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_account_invalid(self, user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
        Endpoint.CREATE_ACCOUNT,
        ResponseSpecs.request_conflict()
        ).post()
        return response


    def deposit_account(self, deposit_request: DepositAccountRequest, user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response


    def deposit_account_invalid(self, deposit_request: DepositAccountRequest, user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_request)
        return response

    def transfer_account(self, transfer_request: TransferAccountRequest, user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response

    def transfer_account_invalid(self, transfer_request: TransferAccountRequest, user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(transfer_request)
        return response

    def credit_user_valid(self, credit_user_request: CreditUserRequest, user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.CREDIT_USER,
            ResponseSpecs.request_created()
        ).post(credit_user_request)
        return response

    def credit_user_invalid(self, credit_user_request: CreditUserRequest, user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.CREDIT_USER,
            ResponseSpecs.request_bad()
        ).post(credit_user_request)
        return response


    def credit_user_repay(self, credit_user_repay: RepayUserRequest, user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_ok()
        ).post(credit_user_repay)
        return response

    def credit_user_repay_invalid(self, credit_user_repay: RepayUserRequest, user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(
                username=user_request.username,
                password=user_request.password
            ),
            Endpoint.REPAY_CREDIT,
            ResponseSpecs.request_unprocessable_entity()
        ).post(credit_user_repay)
        return response