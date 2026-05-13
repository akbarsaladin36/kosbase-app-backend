from fastapi import APIRouter
from src.controllers.room_controller import RoomController
from src.responses.room_response import RoomsMessageResponse, RoomMessageResponse, CreateRoomMessageResponse, UpdateRoomMessageResponse

router = APIRouter()

router.add_api_route(
    path="/",
    endpoint=RoomController.get_rooms_by_user_controller,
    methods=["GET"],
    response_model=RoomsMessageResponse,
    summary="Get all rooms data by owner [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{room_code}",
    endpoint=RoomController.get_room_controller,
    methods=["GET"],
    response_model=RoomMessageResponse,
    summary="Get A detail room data information [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/",
    endpoint=RoomController.create_room_controller,
    methods=["POST"],
    response_model=CreateRoomMessageResponse,
    summary="Create a new room data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{room_code}",
    endpoint=RoomController.update_room_controller,
    methods=["PATCH"],
    response_model=UpdateRoomMessageResponse,
    summary="Update an existing room data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)

router.add_api_route(
    path="/{room_code}",
    endpoint=RoomController.delete_room_controller,
    methods=["DELETE"],
    response_model=UpdateRoomMessageResponse,
    summary="Delete an existing room data [Owner Only]",
    openapi_extra={"security":[{"BearerAuth": []}]}
)