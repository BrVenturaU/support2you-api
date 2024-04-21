import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dependency_injector import containers, providers

from data.database import Database
from features.tickets import tickets_controller
from features.messages import messages_controller

class DependencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[])
    configuration = providers.Configuration()

    # Services
    db = providers.Singleton(Database, connection=configuration.connection_string)

def configure_services(container: DependencyContainer):
    pass # Configure implementations of Services

def add_configuration_providers(container: DependencyContainer):
    APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT")

    try:
        # Default app configurations
        container.configuration.from_yaml(f"config.yaml")

        # Environmental app configurations
        config_filename = f"config.{APP_ENVIRONMENT}.yaml"
        container.configuration.from_yaml(config_filename)
    except Exception:
        pass # TODO: Add logguer
    # Environment and constant value configurations
    container.configuration.env.from_value(APP_ENVIRONMENT)
    container.configuration.connection_string.from_env('APP_DB_CONNECTION')

def configure_pipeline(app: FastAPI) -> FastAPI:
    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routes
    app.include_router(tickets_controller.router)
    app.include_router(messages_controller.router)

    return app