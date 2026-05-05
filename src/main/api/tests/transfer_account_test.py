import pytest
from sqlalchemy.orm import Session

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.db.crud.transaction_crud import TransactionCrudDb as Transaction


@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account(self,
                              api_manager,
                              user_transfer_request,
                              db_session: Session):

        transfer_response = api_manager.user_steps.transfer_account(
            user_transfer_request.transfer_account_request,
            user_transfer_request.user
        )

        assert transfer_response.fromAccountIdBalance == user_transfer_request.deposit_account_request.amount - user_transfer_request.transfer_account_request.amount

        transfer_from_db = Transaction.get_transaction_by_id(db_session, user_transfer_request.transfer_account_request.fromAccountId)

        assert transfer_from_db is not None, "Транзакция перевода не найдена в БД"
        assert transfer_from_db.from_account_id == user_transfer_request.transfer_account_request.fromAccountId


    def test_transfer_account_invalid(self,
                                      api_manager,
                                      user_transfer_request):
        user_transfer_request.transfer_account_request.amount = 499

        api_manager.user_steps.transfer_account_invalid(
            user_transfer_request.transfer_account_request,
            user_transfer_request.user
        )

