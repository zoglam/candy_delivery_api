from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from models.schema.couriers import (
    CourierList,
    Courier,
)
from models.db.couriers import CourierView

couriers_router = APIRouter()


@couriers_router.post('/', status_code=201)
async def create_courier(list: CourierList):
    error_list = []
    valid_list = []

    for courier in list.data:
        try:
            valid_list.append({"id": Courier(**courier).courier_id})
        except ValidationError:
            error_list.append({"id": dict(courier)['courier_id']})

    if error_list:
        return JSONResponse(
            {'validation_error': {'couriers': error_list}},
            status_code=400
        )

    await CourierView.create_couriers(
        [Courier(**c) for c in list.data]
    )

    return {"couriers": valid_list}


@couriers_router.patch('/{courier_id}', status_code=200)
async def change_courier():
    return [{"func": "change_courier"}]


@couriers_router.get('/{courier_id}', status_code=200)
async def get_courier():
    return [{"func": "get_courier"}]
