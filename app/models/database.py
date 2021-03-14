import os
import databases
from enum import Enum, unique
from sqlalchemy import create_engine, MetaData
from sqlalchemy import (
    Table, Column, ForeignKey, Integer, Float, TIMESTAMP,
    Enum as MySQLEnum
)
from sqlalchemy.sql.sqltypes import TIME

metadata = MetaData()

DATABASE_URL = os.getenv('DATABASE_URL')


@unique
class CourierType(Enum):
    foot = 'foot'
    bike = 'bike'
    car = 'car'


couriers_table = Table(
    "couriers",
    metadata,
    Column("courier_id", Integer, primary_key=True),
    Column("courier_type", MySQLEnum(CourierType, name='courier_type')),
)

orders_table = Table(
    "orders",
    metadata,
    Column("order_id", Integer, primary_key=True),
    Column("weight", Float),
    Column("region", Integer),
    Column("delivery_hours", TIMESTAMP),
)

regions_table = Table(
    "regions",
    metadata,
    Column("region_connection_id", Integer,
           primary_key=True, autoincrement=True),
    Column("region_id", Integer),
    Column("courier_id", Integer, ForeignKey('couriers.courier_id')),
)

courier_hours_table = Table(
    "courier_hours",
    metadata,
    Column("hour_id", Integer, primary_key=True, autoincrement=True),
    Column("start_time", TIME),
    Column("end_time", TIME),
)

order_hours_table = Table(
    "order_hours",
    metadata,
    Column("hour_id", Integer, primary_key=True),
    Column("start_time", TIME),
    Column("end_time", TIME),
    Column("order_id", Integer, ForeignKey('orders.order_id')),
)

engine = create_engine(
    DATABASE_URL.replace('mysql', 'mysql+mysqlconnector'),
    echo=True
)

database = databases.Database(DATABASE_URL)
metadata.drop_all(engine)
metadata.create_all(engine)
