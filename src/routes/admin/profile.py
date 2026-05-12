from fastapi import APIRouter
from src.controllers.profile_controller import ProfileController
from src.responses.profile_response import ProfileMessageResponse

router = APIRouter()

router.add_api_route(
    path="/",
    endpoint=ProfileController.get_profile_controller,
    methods=["GET"],
    response_model=ProfileMessageResponse,
    summary="Get a profile detail information data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/",
    endpoint=ProfileController.update_profile_controller,
    methods=["PATCH"],
    response_model=ProfileMessageResponse,
    summary="Update a profile data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)
