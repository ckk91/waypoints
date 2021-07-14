"""
Pydantic Schemas for REST API
"""
from typing import List, Optional

from pydantic import BaseModel, validator


class WaypointBase(BaseModel):
    longitude: float
    latitude: float

    @validator("latitude")
    def lat_range_validator(cls, lat):
        if -85.0 <= lat <= 85.05115:
            return lat
        raise ValueError("Latitude out of bounds.")

    @validator("longitude")
    def lon_range_validator(cls, lon):
        if -180.0 <= lon <= 180.0:
            return lon
        raise ValueError("Longitude out of bounds.")


class Waypoint(WaypointBase):
    id: int

    class Config:
        orm_mode = True


class PagedWaypoints(BaseModel):
    total: Optional[int]
    values: List[Waypoint]
