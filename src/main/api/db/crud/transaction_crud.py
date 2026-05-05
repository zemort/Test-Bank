from sqlalchemy.orm import Session
from src.main.api.db.models.transaction_model import Transaction


class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_id(db: Session, from_account_id: int) -> Transaction | None:
        return db.query(Transaction).filter_by(from_account_id=from_account_id).order_by(Transaction.created_at.desc()).first()