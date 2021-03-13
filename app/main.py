from fastapi import FastAPI

from app.api.couriers import couriers
from app.api.orders import orders
from app.models import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(couriers, prefix='/api/couriers')
app.include_router(orders, prefix='/api/orders')
