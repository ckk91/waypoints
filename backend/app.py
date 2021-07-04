"""
Minimal backend server using fastapi to store and retrieve waypoints
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .db import Base, engine
from .routes import router

STATIC_PATH = f"{Path(__file__).parent.absolute()}/static"


def build_app(app: FastAPI):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.mount(
        "/static", StaticFiles(directory=STATIC_PATH, html=True), name="static"
    )  # serving FE

    app.include_router(router)

    @app.on_event("startup")
    async def startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    return app


app = build_app(FastAPI())
