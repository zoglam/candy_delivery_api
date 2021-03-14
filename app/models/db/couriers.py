from models.database import (
    database,
    couriers_table,
    regions_table,
    courier_hours_table
)
from models.schema.couriers import Courier
from typing import List


class CourierView:

    @staticmethod
    async def create_couriers(couriers: List[Courier]):
        for courier in couriers:
            print(couriers)
            print(courier)
            query = couriers_table.insert().values(
                courier_id=courier.courier_id,
                courier_type=courier.courier_type
            )
            await database.execute(query=query)

            for region in courier.regions:
                query = regions_table.insert().values(
                    region_id=region,
                    courier_id=courier.courier_id
                )
                await database.execute(query=query)

            for hours in courier.working_hours:
                start_time, end_time = hours.split('-')
                query = courier_hours_table.insert().values(
                    start_time=start_time,
                    end_time=end_time
                )
                await database.execute(query=query)
