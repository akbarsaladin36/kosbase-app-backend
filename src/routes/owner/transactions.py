from fastapi import APIRouter
from src.controllers.transaction_controller import TransactionController
from src.responses.transaction_response import TransactionsMessageResponse, TransactionMessageResponse

router = APIRouter()

router.add_api_route(
    path="/",
    endpoint=TransactionController.get_transactions_by_owner_controller,
    methods=["GET"],
    response_model=TransactionsMessageResponse,
    summary="Get all transactions by owner data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{transaction_code}",
    endpoint=TransactionController.get_transaction_controller,
    methods=["GET"],
    response_model=TransactionMessageResponse,
    summary="Get a transaction detail information data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/",
    endpoint=TransactionController.create_transaction_controller,
    methods=["POST"],
    response_model=TransactionMessageResponse,
    summary="Create a new transaction data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{transaction_code}",
    endpoint=TransactionController.update_transaction_controller,
    methods=["PATCH"],
    response_model=TransactionMessageResponse,
    summary="Update an existing transaction data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{transaction_code}",
    endpoint=TransactionController.delete_transaction_controller,
    methods=["DELETE"],
    response_model=TransactionMessageResponse,
    summary="Delete an existing transaction data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)