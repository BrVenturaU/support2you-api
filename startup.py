from dependency_injector import containers, providers

class DependencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[])
    configuration = providers.Configuration()

    # Services

def configure_services(container: DependencyContainer):
    pass # Configure implementations of Services

def add_app_configuration(container: DependencyContainer):
    pass # Add app configuration.