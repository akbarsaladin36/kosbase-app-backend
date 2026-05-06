from fastapi import APIRouter
from src.controllers.resident_controller import ResidentController
from src.responses.resident_response import ResidentsResponse, ResidentResponse, UpdateResidentMessageResponse

router = APIRouter()

router.add_api_route(
    path="/",
    endpoint=ResidentController.get_residents_by_owner_controller,
    methods=["GET"],
    response_model=ResidentsResponse,
    summary="Get all residents data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth":[]}]}
)

router.add_api_route(
    path="/{resident_uuid}",
    endpoint=ResidentController.get_resident_controller,
    methods=["GET"],
    response_model=ResidentResponse,
    summary="Get a resident detail information data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth":[]}]}
)

router.add_api_route(
    path="/",
    endpoint=ResidentController.create_resident_controller,
    methods=["POST"],
    response_model=ResidentResponse,
    summary="Create a new resident data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth":[]}]}
)

router.add_api_route(
    path="/{resident_uuid}",
    endpoint=ResidentController.update_resident_controller,
    methods=["PATCH"],
    response_model=UpdateResidentMessageResponse,
    summary="Update an existing resident data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth":[]}]}
)

router.add_api_route(
    path="/{resident_uuid}",
    endpoint=ResidentController.delete_resident_controller,
    methods=["DELETE"],
    response_model=ResidentResponse,
    summary="Delete an existing resident data [Admin Only]",
    openapi_extra={"security":[{"BearerAuth":[]}]}
)