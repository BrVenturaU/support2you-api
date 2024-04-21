import os
from dependency_injector import containers, providers

class DependencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[])
    configuration = providers.Configuration()

    # Services

def configure_services(container: DependencyContainer):
    pass # Configure implementations of Services

def add_app_configuration(container: DependencyContainer):
    APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT")

    # Default app configurations
    container.configuration.from_yaml(f"config.yaml")

    # Environmental app configurations
    config_filename = f"config.{APP_ENVIRONMENT}.yaml"
    container.configuration.from_yaml(config_filename)

    # Environment and constant value configurations
    container.configuration.env.from_value(APP_ENVIRONMENT)