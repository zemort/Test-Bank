import pytest
from sqlalchemy.orm import Session

from src.main.api.models.credit_account_fixture_model import CreditAccountFixtureModel
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit



@pytest.mark.api
class TestUserCredit:
    def test_user_credit(self,
                         api_manager,
                         user_credit_request: CreditAccountFixtureModel,
                         db_session: Session):

        credit_response = api_manager.user_steps.credit_user_valid(
            user_credit_request.credit_request,
            user_credit_request.user
        )

        assert credit_response.balance == user_credit_request.credit_request.amount

        credit_from_db = Credit.get_credit_by_credit_id(db_session, credit_response.creditId)

        assert credit_from_db is not None, "Кредит не найден в БД"
        assert credit_from_db.id == credit_response.creditId, "id кредита не совпадает с id из ответа"


    def test_user_credit_invalid(self,
                                 api_manager,
                                 user_credit_request: CreditAccountFixtureModel):
        user_credit_request.credit_request.amount = 1000

        api_manager.user_steps.credit_user_invalid(
            user_credit_request.credit_request,
            user_credit_request.user
        )