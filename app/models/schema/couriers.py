import re
from pydantic import BaseModel, validator
from typing import List


class Courier(BaseModel):
    courier_id: int
    courier_type: str
    regions: List[int]
    working_hours: List[str]

    @validator('courier_type')
    def courier_type_must_valid(cls, v):
        if v not in ('foot', 'bike', 'car'):
            raise ValueError("must be foot, bike or car")
        return v

    @validator('working_hours')
    def working_hours_valid_format(cls, v):
        time_patt = re.compile(
            r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]' +
            r'\-' +
            r'([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
        )
        for hours in v:
            if time_patt.search(hours) is None:
                raise ValueError("invalid time format")
        return v


class CourierList(BaseModel):
    data: List
