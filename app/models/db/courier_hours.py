from app.models.database import (
    database,
    courier_hours_table,
)


class CourierHoursView:

    @staticmethod
    async def create_courier_hours(start_time: str, end_time: str):
        query = courier_hours_table.insert().values(
            start_time=start_time,
            end_time=end_time
        )
        await database.execute(query=query)
