from fastapi import APIRouter

orders_router = APIRouter()


@orders_router.post('/', status_code=201)
async def create_order():
    return [{"func": "create_order"}]


@orders_router.post('/assign', status_code=200)
async def assign_order():
    return [{"func": "assign_order"}]


@orders_router.post('/complete', status_code=200)
async def complete_order():
    return [{"func": "complete_order"}]
