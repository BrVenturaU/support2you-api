from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

from startup import DependencyContainer, configure_services, add_app_configuration
from data import ensure_db_exists

from features.tickets import tickets_controller
from features.messages import messages_controller

def create_app() -> FastAPI:
    load_dotenv()
    ensure_db_exists()

    container = DependencyContainer()
    add_app_configuration(container)
    configure_services(container)

    app = FastAPI()
    app.container = container

    # Include routes here
    app.include_router(tickets_controller.router)
    app.include_router(messages_controller.router)

    return app

app = create_app()

@app.middleware("http")
async def redirect(request: Request, next):
    if(request.url.path == "/"):
        return RedirectResponse("/docs")
    
    return await next(request)