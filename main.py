from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from startup import (
    DependencyContainer,
    configure_services,
    add_configuration_providers
)
from data import ensure_db_exists
from features.tickets import tickets_controller
from features.messages import messages_controller


def create_app() -> FastAPI:
    load_dotenv()
    ensure_db_exists()

    container = DependencyContainer()
    add_configuration_providers(container)
    configure_services(container)

    app = FastAPI()

    app.container = container
    return app

def configure_pipeline(app: FastAPI) -> FastAPI:
    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes
    app.include_router(tickets_controller)
    app.include_router(messages_controller)

    return app

app = create_app()

configure_pipeline(app)

@app.middleware("http")
async def redirect(request: Request, next):
    if(request.url.path == "/"):
        return RedirectResponse("/docs")
    
    return await next(request)