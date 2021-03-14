from pydantic import BaseModel, validator
from typing import List


class Courier(BaseModel):
    courier_id: int
    courier_type: str
    regions: List[int]
    working_hours: List[str]

    @validator('courier_type')
    def courier_type_must_(cls, v):
        if v not in ('foot', 'bike', 'car'):
            raise ValueError("must be foot, bike or car")
        return v


class CourierList(BaseModel):
    data: List
