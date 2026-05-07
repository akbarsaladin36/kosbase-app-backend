from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.room_repository import RoomRepository
from src.repositories.user_repository import UserRepository
from src.services.transaction_service import TransactionService
from src.config.database import get_db
from src.inputs.transaction_input import CreateTransactionInput, UpdateTransactionInput

def get_transaction_service(db: Session = Depends(get_db)) -> TransactionService:
    transactionRepository = TransactionRepository(db)
    roomRepository = RoomRepository(db)
    userRepository = UserRepository(db)
    return TransactionService(transactionRepository, roomRepository, userRepository)

class TransactionController:
    @staticmethod
    def get_transactions_controller(transactionService: TransactionService = Depends(get_transaction_service)):
        return transactionService.get_transactions_service()
    
    @staticmethod
    def get_transactions_by_owner_controller(req: Request, transactionService: TransactionService = Depends(get_transaction_service)):
        current_user = req.state.current_user
        return transactionService.get_transactions_by_owner_service(current_user)
    
    @staticmethod
    def get_transactions_by_user_controller(req: Request, transactionService: TransactionService = Depends(get_transaction_service)):
        current_user = req.state.current_user
        return transactionService.get_transactions_by_user_service(current_user)
    
    @staticmethod
    def get_transaction_controller(transaction_code: str, transactionService: TransactionService = Depends(get_transaction_service)):
        return transactionService.get_transaction_service(transaction_code)
    
    @staticmethod
    def create_transaction_controller(req: Request, payload: CreateTransactionInput, transactionService: TransactionService = Depends(get_transaction_service)):
        current_user = req.state.current_user
        return transactionService.create_transaction_service(payload, current_user)
    
    @staticmethod
    def update_transaction_controller(transaction_code: str, req: Request, payload: UpdateTransactionInput, transactionService: TransactionService = Depends(get_transaction_service)):
        current_user = req.state.current_user
        return transactionService.update_transaction_service(transaction_code, payload, current_user)
    
    @staticmethod
    def delete_transaction_controller(transaction_code: str, transactionService: TransactionService = Depends(get_transaction_service)):
        return transactionService.delete_transaction_service(transaction_code)
