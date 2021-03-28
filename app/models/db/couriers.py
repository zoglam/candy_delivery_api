import sqlalchemy
from app.models.database import (
    database,
    couriers_table,
)
from app.models.schema.couriers import Courier
from app.models.db.regions import RegionsView
from app.models.db.courier_hours import CourierHoursView


class CourierView:

    @staticmethod
    async def create_courier(courier: Courier):
        query = couriers_table.insert().values(
            courier_id=courier.courier_id,
            courier_type=courier.courier_type
        )
        await database.execute(query=query)

        for region in courier.regions:
            RegionsView.create_region(region, courier)

        for hours in courier.working_hours:
            start_time, end_time = hours.split('-')
            CourierHoursView.create_courier_hours(start_time, end_time)

    @staticmethod
    async def get_courier(courier_id: int):
        id = sqlalchemy.sql.column('courier_id')
        query = couriers_table.select().where(
            id == courier_id
        )
        return await database.fetch_one(query=query)
