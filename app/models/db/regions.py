from app.models.database import (
    database,
    regions_table,
)
from app.models.schema.couriers import Courier


class RegionsView:

    @staticmethod
    async def create_region(region: int, courier: Courier):
        query = regions_table.insert().values(
            region_id=region,
            courier_id=courier.courier_id
        )
        await database.execute(query=query)
