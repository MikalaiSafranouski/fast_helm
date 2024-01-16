import logging
from typing import AsyncIterator

from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_ECHO

logger = logging.getLogger(__name__)


meta = MetaData()

class Base(DeclarativeBase):
    """1"""
    metadata = meta

async_engine = create_async_engine(
    url=SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    echo=SQLALCHEMY_ECHO,
)

async_session = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    future=True,
    expire_on_commit=False,
)


async def get_session() -> AsyncIterator[async_sessionmaker]:
    """1"""
    try:
        yield async_session
    except SQLAlchemyError as exc:
        logger.exception(exc)
