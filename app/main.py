from fastapi import FastAPI

from app.api.couriers import couriers_router
from app.api.orders import orders_router
from app.models.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(couriers_router, prefix='/api/couriers', tags=['couriers'])
app.include_router(orders_router, prefix='/api/orders', tags=['orders'])
