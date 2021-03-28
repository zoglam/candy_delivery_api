from app.models.db.couriers import CourierView
from typing import List
from app.models.schema.couriers import (
    Courier,
)


class DBManager:

    @staticmethod
    async def existed_couriers_from(couriers: List[Courier]):
        existed_couriers = []

        for courier in couriers:
            id = courier['courier_id']
            try:
                if await CourierView.get_courier(id) is not None:
                    raise Exception(f'id: {id} exist')
            except Exception:
                existed_couriers.append({"id": id})
        return existed_couriers
