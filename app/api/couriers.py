from fastapi import APIRouter

couriers = APIRouter()


@couriers.post('/')
async def create_courier():
    return [{"func": "create_courier"}]


@couriers.patch('/{courier_id}/')
async def change_courier():
    return [{"func": "change_courier"}]


@couriers.get('/{courier_id}/')
async def get_courier():
    return [{"func": "get_courier"}]
