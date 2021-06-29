"""
Pydantic Schemas for REST API
"""
import re
from typing import List, Optional, Tuple

from pydantic import BaseModel
from pydantic.types import constr  # todo add to decisions.md

RE_WAYPOINT = r"^(-?\d+\.\d+),? +(-?\d+\.\d+)$"
RE_WAYPOINT_COMPILED = re.compile(RE_WAYPOINT)


class NotAValidCoordinateError(BaseException):
    pass


async def parse_input(raw_wp: str) -> Tuple[float, float]:
    (lat, lon) = RE_WAYPOINT_COMPILED.findall(raw_wp)[0]
    lat, lon = float(lat), float(lon)
    if -85.0 <= lat <= 85.05115 and -180.0 <= lon <= 180.0:
        return (lat, lon)
    raise NotAValidCoordinateError()


class WaypointString(BaseModel):
    waypoint: constr(regex=RE_WAYPOINT)


class WaypointBase(BaseModel):
    longitude: float
    latitude: float


class Waypoint(WaypointBase):
    id: int

    class Config:
        orm_mode = True


class PagedWaypoints(BaseModel):
    total: Optional[int]
    values: List[Waypoint]
