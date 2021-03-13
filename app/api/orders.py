from fastapi import APIRouter

orders = APIRouter()


@orders.post('/')
async def create_order():
    return [{"func": "create_order"}]


@orders.post('/assign/')
async def assign_order():
    return [{"func": "assign_order"}]


@orders.post('/complete/')
async def complete_order():
    return [{"func": "complete_order"}]
