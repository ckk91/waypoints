"""
db connector and model
"""

import sqlalchemy
from sqlalchemy import Column, Float, Integer
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.pool import NullPool

from .config import CONFIG

Base = declarative_base()


class WaypointModel(Base):
    __tablename__ = "waypoints"
    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)

    @staticmethod
    async def create_waypoint(db: Session, lat: float, long: float):
        wp = WaypointModel(longitude=long, latitude=lat)
        db.add(wp)
        await db.commit()
        return wp

    @staticmethod
    async def get_table_size(db: Session):
        return await db.run_sync(lambda session: session.query(WaypointModel).count())

    @staticmethod
    async def get_paged(db: Session, offset: int = 0, limit: int = 10):
        limit = (
            limit
            if limit <= CONFIG.get("MAX_PAGINATION")
            else CONFIG.get("MAX_PAGINATION")
        )
        return await db.run_sync(
            lambda session: session.query(WaypointModel)
            .offset(offset)
            .limit(limit)
            .all()
        )


engine = create_async_engine(
    f"postgresql+asyncpg://postgres:example@{CONFIG.get('DB_HOST')}",
)

Session_ = sqlalchemy.orm.sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session():
    async with Session_() as session:
        async with session.begin():
            yield session
