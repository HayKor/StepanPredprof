from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.core.dependencies.fastapi import TemplatesDependency


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, templates: TemplatesDependency):
    return templates.TemplateResponse("index.html", {"request": request, "name": "World"})


@router.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, templates: TemplatesDependency, name: str):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})
