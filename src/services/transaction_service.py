from fastapi import Depends, HTTPException, status
from datetime import datetime
from src.repositories.transaction_repository import TransactionRepository
from src.repositories.room_repository import RoomRepository
from src.repositories.user_repository import UserRepository
from src.repositories.payment_repository import PaymentRepository
from src.inputs.transaction_input import CreateTransactionInput, UpdateTransactionInput
from src.responses.transaction_response import TransactionResponse, TransactionMessageResponse, TransactionsMessageResponse
from src.helper.index import generate_code

class TransactionService:
    def __init__(self, transactionRepository: TransactionRepository, roomRepository: RoomRepository, userRepository: UserRepository, paymentRepository: PaymentRepository):
        self.transactionRepository = transactionRepository
        self.roomRepository = roomRepository
        self.userRepository = userRepository
        self.paymentRepository = paymentRepository

    def get_transactions_service(self) -> TransactionsMessageResponse:
        transactions = self.transactionRepository.get_transactions_repository()

        if len(transactions) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All transactions are empty!"
            )
        else:
            return TransactionsMessageResponse(
                status_code=status.HTTP_200_OK,
                message="All transactions are succesfully appeared!",
                data=transactions
            )
        
    def get_transactions_by_owner_service(self, current_user: dict) -> TransactionsMessageResponse:
        owner_uuid = current_user.get("uuid")
        transactions = self.transactionRepository.get_transactions_by_owner_repository(owner_uuid)

        if len(transactions) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All transactions by owner are empty!"
            )
        else:
            return TransactionsMessageResponse(
                status_code=status.HTTP_200_OK,
                message="All transactions by owner are succesfully appeared!",
                data=transactions
            )
        
    def get_transactions_by_user_service(self, current_user: dict) -> TransactionsMessageResponse:
        user_uuid = current_user.get("uuid")
        transactions = self.transactionRepository.get_transactions_by_user_repository(user_uuid)

        if len(transactions) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="All transactions by user are empty!"
            )
        else:
            return TransactionsMessageResponse(
                status_code=status.HTTP_200_OK,
                message="All transactions by user are succesfully appeared!",
                data=transactions
            )
        
    def get_transaction_service(self, transaction_code: str) -> TransactionMessageResponse:
        transaction = self.transactionRepository.get_transaction_repository(transaction_code)

        if transaction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A transaction data is not found!"
            )
        else:
            return TransactionMessageResponse(
                status_code=status.HTTP_200_OK,
                message="A transaction data is succesfully appeared!",
                data=transaction
            )
        
    def create_transaction_service(self, payload: CreateTransactionInput, current_user: dict) -> TransactionMessageResponse:
        check_owner = self.userRepository.get_user_by_id_repository(payload.owner_uuid)

        if check_owner is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="An owner data is not found"
            )


        check_room = self.roomRepository.get_room_repository(payload.room_code)

        if check_room is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A room data is not found"
            )
        
        check_resident = self.transactionRepository.get_resident_for_transaction_repository(payload.user_uuid)

        if check_resident is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="A user data is not found"
            )
        create_transaction_setdata = payload.model_dump()
        create_transaction_setdata["code"] = generate_code("TC")
        create_transaction_setdata["total_price"] = payload.base_price - payload.discount_price if payload.discount_price > 0 else payload.base_price 
        create_transaction_setdata["status_cd"] = "pending"
        create_transaction_setdata["created_at"] = datetime.now()
        create_transaction_setdata["created_by"] = current_user.get("uuid")
        create_transaction_setdata["created_by_username"] = current_user.get("username")
        create_transaction = self.transactionRepository.create_transaction_repository(create_transaction_setdata)

        create_payment_setdata = {
            "user_uuid": create_transaction.user_uuid,
            "transaction_code": create_transaction.code,
            "code": generate_code("PC"),
            "description": f"Pembayaran dari {create_transaction.description}",
            "total_price": create_transaction.total_price,
            "status_cd": "pending",
            "created_at": datetime.now(),
            "created_by": current_user.get("uuid"),
            "created_by_username": current_user.get("username"),
        }

        self.paymentRepository.create_payment_repository(create_payment_setdata)

        validate_create_transaction = TransactionResponse.model_validate(create_transaction)
        return TransactionMessageResponse(
            status_code=status.HTTP_200_OK,
            message="A new transaction is succesfully appeared!",
            data=validate_create_transaction
        )
    
    def update_transaction_service(self, transaction_code: str, payload: UpdateTransactionInput, current_user: dict) -> TransactionMessageResponse:
        transaction = self.transactionRepository.get_transaction_repository(transaction_code)

        if transaction is None:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="A transaction data is not found!"
            )
        else:
            update_transaction_setdata = payload.model_dump()
            update_transaction_setdata["updated_at"] = datetime.now()
            update_transaction_setdata["updated_by"] = current_user.get("uuid")
            update_transaction_setdata["updated_by_username"] = current_user.get("username")
            update_transaction = self.transactionRepository.update_transaction_repository(transaction, update_transaction_setdata)

            payments = self.paymentRepository.get_payment_by_transaction_repository(transaction.code)

            if payments is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="A payment data is not found!"
                )

            update_payment_setdata = {
                "status_cd": update_transaction.status_cd,
                "updated_at": datetime.now(),
                "updated_by": current_user.get("uuid"),
                "updated_by_username": current_user.get("username"), 
            }

            for payment in payments:
                self.paymentRepository.update_payment_repository(payment, update_payment_setdata)

            validate_update_transaction = TransactionResponse.model_validate(update_transaction)
            return TransactionMessageResponse(
                status_code=status.HTTP_200_OK,
                message="An existing transaction data is succesfully updated!",
                data=validate_update_transaction
            )
        
    def delete_transaction_service(self, transaction_code: str) -> TransactionMessageResponse:
        transaction = self.transactionRepository.get_transaction_repository(transaction_code)

        if transaction is None:
            raise HTTPException(
                status_code=status.HTTP_200_OK,
                detail="A transaction data is not found!"
            )
        else:
            self.transactionRepository.delete_transaction_repository(transaction)
            return TransactionMessageResponse(
                status_code=status.HTTP_200_OK,
                message="An existing transaction data is succesfully deleted!",
            )
    