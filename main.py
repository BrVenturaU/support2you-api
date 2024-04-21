from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

from startup import (
    DependencyContainer,
    configure_services,
    add_configuration_providers,
    configure_pipeline
)
from data import ensure_db_exists


def create_app() -> FastAPI:
    load_dotenv()
    ensure_db_exists()

    container = DependencyContainer()
    add_configuration_providers(container)
    configure_services(container)

    app = FastAPI()

    app.container = container
    return app

app = create_app()

configure_pipeline(app)

@app.middleware("http")
async def redirect(request: Request, next):
    if(request.url.path == "/"):
        return RedirectResponse("/docs")
    
    return await next(request)