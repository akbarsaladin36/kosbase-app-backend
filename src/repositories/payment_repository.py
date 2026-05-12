from sqlalchemy.orm import Session
from src.models.payment_models import Payment

class PaymentRepository:
    def __init__(self, db = Session):
        self.db = db

    def get_payments_repository(self) -> tuple[list[Payment]]:
        payments = self.db.query(Payment).all()
        return payments
    
    def get_payment_repository(self, payment_code: str) -> Payment:
        payment = self.db.query(Payment).filter(Payment.code == payment_code).first()
        return payment
    
    def get_payment_by_transaction_repository(self, transaction_code: str) -> Payment:
        payment = self.db.query(Payment).filter(Payment.transaction_code == transaction_code).all()
        return payment
    
    def create_payment_repository(self, create_payment_input: dict) -> Payment:
        payment = Payment(**create_payment_input)
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment
    
    def update_payment_repository(self, payment: Payment, update_payment_input: dict) -> tuple[list[Payment]]:
        for field, value in update_payment_input.items():
            setattr(payment, field, value)
        self.db.commit()
        self.db.refresh(payment)
        return payment
    
    def delete_payment_repository(self, payment: Payment) -> None:
        self.db.delete(payment)
        self.db.commit()