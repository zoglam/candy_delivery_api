from fastapi import APIRouter
from pydantic import ValidationError
from app.models.schema.couriers import (
    CourierList,
    Courier,
)
from app.models.db.couriers import CourierView
from app.api.db_manager import DBManager
from app.api.error import APIError

couriers_router = APIRouter()


@couriers_router.post('/', status_code=201)
async def create_courier(list: CourierList):
    error_list = []
    valid_list = []

    for courier in list.data:
        try:
            valid_list.append({"id": Courier(**courier).courier_id})
        except ValidationError:
            error_list.append({"id": courier['courier_id']})
    if error_list:
        return APIError.create_courier_error(error_list)

    error_list = await DBManager.existed_couriers_from(list.data)
    if error_list:
        return APIError.create_courier_error(error_list)

    for courier in list.data:
        await CourierView.create_courier(Courier(**courier))

    return {"couriers": valid_list}


@couriers_router.patch('/{courier_id}', status_code=200)
async def change_courier():
    return [{"func": "change_courier"}]


@couriers_router.get('/{courier_id}', status_code=200)
async def get_courier():
    return [{"func": "get_courier"}]
