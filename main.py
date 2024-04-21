from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv

from startup import DependencyContainer, configure_services, add_app_configuration


def create_app() -> FastAPI:
    load_dotenv()
    container = DependencyContainer()
    add_app_configuration(container)
    configure_services(container)

    app = FastAPI()
    app.container = container

    # Include routes here


    return app

app = create_app()

@app.middleware("http")
async def redirect(request: Request, next):
    if(request.url.path == "/"):
        return RedirectResponse("/docs")
    
    return await next(request)