from contextlib import asynccontextmanager, contextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.core.config import AppConfig
from app.core.dependencies import constructors as app_depends, fastapi as stubs

from .routers.router import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    config = AppConfig.from_env()
    templates = Jinja2Templates(directory="app/templates")
    with contextmanager(app_depends.db_session_maker)(config.database.url) as maker:
        app.dependency_overrides[stubs.app_config_stub] = lambda: config
        app.dependency_overrides[stubs.db_session_maker_stub] = lambda: maker
        app.dependency_overrides[stubs.templates_stub] = lambda: templates

        yield


app = FastAPI(
    lifespan=lifespan,
)


app.include_router(router)
