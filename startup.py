import os
from dependency_injector import containers, providers

from data.database import Database
from services.chat_service import BaseChatService, ChatService, MockedChatService


class DependencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["features.tickets", "features.messages"]
    )
    configuration = providers.Configuration()

    # Services
    db = providers.Singleton(Database, connection=configuration.connection_string)
    chat_service = providers.AbstractFactory(BaseChatService)


def configure_services(container: DependencyContainer):
    if container.configuration.isProd():
        container.chat_service.override(
            providers.Factory(
                ChatService,
                sys_prompt=container.configuration.openai_api.system,
                model=container.configuration.openai_api.model,
                temperature=container.configuration.openai_api.temperature,
            )
        )

    else:
        container.chat_service.override(
            providers.Factory(
                MockedChatService,
                sys_prompt=container.configuration.openai_api.system,
                model=container.configuration.openai_api.model,
                temperature=container.configuration.openai_api.temperature,
            )
        )


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
    container.configuration.isDev.from_value(APP_ENVIRONMENT == "development")
    container.configuration.isProd.from_value(APP_ENVIRONMENT == "production")
    container.configuration.connection_string.from_env("APP_DB_CONNECTION")
