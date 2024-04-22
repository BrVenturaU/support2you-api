import os
from dependency_injector import containers, providers

from data.database import Database
from services.chat_service import ChatService


class DependencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["features.tickets", "features.messages"]
    )
    configuration = providers.Configuration()

    # Services
    db = providers.Singleton(Database, connection=configuration.connection_string)
    chat_service = providers.Factory(
        ChatService,
        sys_prompt=configuration.openai_api.system,
        model=configuration.openai_api.model,
        temperature=configuration.openai_api.temperature,
    )


def configure_services(container: DependencyContainer):
    pass  # Configure implementations of Services


def add_configuration_providers(container: DependencyContainer):
    APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT")

    try:
        # Default app configurations
        container.configuration.from_yaml(f"config.yaml")

        # Environmental app configurations
        config_filename = f"config.{APP_ENVIRONMENT}.yaml"
        container.configuration.from_yaml(config_filename)
    except Exception:
        pass  # TODO: Add logguer
    # Environment and constant value configurations
    container.configuration.env.from_value(APP_ENVIRONMENT)
    container.configuration.connection_string.from_env("APP_DB_CONNECTION")
