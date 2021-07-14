from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm.session import Session
from starlette.requests import Request
from starlette.responses import HTMLResponse

from .config import CONFIG
from .db import WaypointModel, get_session
from .schemas import (
    PagedWaypoints,
    Waypoint,
    WaypointBase,
)

router = APIRouter()

app_templates = Jinja2Templates(directory=f"{CONFIG['BASE_DIR']}/templates")


@router.get("/", response_class=HTMLResponse)
async def get_app_index(request: Request):
    return app_templates.TemplateResponse("index.html", {"request": request})


# === create, read, as per requirements ===
@router.get("/waypoints/", response_model=PagedWaypoints)
async def read_paged_waypoints(
    offset=0, limit: int = 10, db: Session = Depends(get_session)
):
    if limit > CONFIG.get("MAX_PAGINATION"):
        raise HTTPException(status_code=422, detail="Limit too large.")

    return PagedWaypoints(
        values=await WaypointModel.get_paged(db, offset=offset, limit=limit),
        total=await WaypointModel.get_table_size(db),
    )  # XXX kinda expensive, but good enough for now


@router.post("/waypoints/", response_model=Waypoint, status_code=201)
async def create_waypoint(waypoint: WaypointBase, db: Session = Depends(get_session)):
    return await WaypointModel.create_waypoint(
        db, long=waypoint.longitude, lat=waypoint.latitude
    )
