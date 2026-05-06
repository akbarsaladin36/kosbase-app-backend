from fastapi import APIRouter
from src.controllers.auth_controller import AuthController
from src.responses.auth_response import RegisterMessageResponse, LoginMessageResponse

router = APIRouter()

router.add_api_route(
    path="/register",
    endpoint=AuthController.register_controller,
    methods=["POST"],
    response_model=RegisterMessageResponse,
    summary="register a new user",
    openapi_extra={"security":[]}
)

router.add_api_route(
    path="/login",
    endpoint=AuthController.login_controller,
    methods=["POST"],
    response_model=LoginMessageResponse,
    summary="login with a registered user",
    openapi_extra={"security":[]}
)

