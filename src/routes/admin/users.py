from fastapi import APIRouter
from src.controllers.user_controller import UserController
from src.responses.user_response import UsersResponse, UserResponse

router = APIRouter()

router.add_api_route(
    path="/",
    endpoint=UserController.get_users_controller,
    methods=["GET"],
    response_model=UsersResponse,
    summary="Get all users data [Admin Only]",
    openapi_extra={ "security":[{"BearerAuth": []}] }
)

router.add_api_route(
    path="/{username}",
    endpoint=UserController.get_user_controller,
    methods=["GET"],
    response_model=UserResponse,
    summary="Get user data information [Admin Only]",
    openapi_extra={ "security":[{"BearerAuth": []}] }
)

router.add_api_route(
    path="/",
    endpoint=UserController.create_user_controller,
    methods=["POST"],
    response_model=UserResponse,
    summary="Create a new user data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{username}",
    endpoint=UserController.update_user_controller,
    methods=["PATCH"],
    response_model=UserResponse,
    summary="Update an existing user data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{username}",
    endpoint=UserController.delete_user_controller,
    methods=["DELETE"],
    response_model=UserResponse,
    summary="Delete an existing user data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

