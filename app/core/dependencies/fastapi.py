from typing import Annotated, Any, AsyncGenerator

from fastapi import Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import AppConfig

from . import constructors as app_depends


def db_session_maker_stub() -> sessionmaker[Any]:
    raise NotImplementedError


def app_config_stub() -> AppConfig:
    raise NotImplementedError


def templates_stub() -> Jinja2Templates:
    raise NotImplementedError


async def db_session(
    request: Request,
    maker: Annotated[sessionmaker[Any], Depends(db_session_maker_stub)],
) -> AsyncGenerator[AsyncSession, None]:
    generator = app_depends.db_session_autocommit(maker)
    session = await anext(generator)
    request.state.db = session

    yield session

    try:
        await anext(generator)
    except StopAsyncIteration:
        pass
    else:
        raise RuntimeError("Database session not closed (db dependency generator is not closed).")


DatabaseDependency = Annotated[AsyncSession, Depends(db_session)]
TemplatesDependency = Annotated[Jinja2Templates, Depends(templates_stub)]
