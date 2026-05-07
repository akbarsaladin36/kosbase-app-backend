from src.models.transaction_models import Transaction
from src.models.resident_models import Resident
from sqlalchemy.orm import Session

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_transactions_repository(self) -> tuple[list[Transaction]]:
        transactions = self.db.query(Transaction).all()
        return transactions
    
    def get_transactions_by_owner_repository(self, owner_uuid: str) -> tuple[list[Transaction]]:
        transactions = self.db.query(Transaction).filter(Transaction.owner_uuid == owner_uuid).all()
        return transactions
    
    def get_transactions_by_user_repository(self, user_uuid: str) -> tuple[list[Transaction]]:
        transactions = self.db.query(Transaction).filter(Transaction.user_uuid == user_uuid).all()
        return transactions
    
    def get_resident_for_transaction_repository(self, resident_uuid: str) -> Resident:
        resident = self.db.query(Resident).filter(Resident.uuid == resident_uuid).first()
        return resident

    def get_transaction_repository(self, transaction_code: str) -> Transaction:
        transaction = self.db.query(Transaction).filter(Transaction.code == transaction_code).first()
        return transaction
    
    def create_transaction_repository(self, create_transaction_input: dict) -> Transaction:
        transaction = Transaction(**create_transaction_input)
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    def update_transaction_repository(self, transaction: Transaction, update_transaction_input: dict) -> Transaction:
        for field,value in update_transaction_input.items():
            setattr(transaction, field, value)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    def delete_transaction_repository(self, transaction: Transaction) -> Transaction:
        self.db.delete(transaction)
        self.db.commit()
    