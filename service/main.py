from service.backend_service import BackendService
from service.configuration.application_configuration import Configuration

config = Configuration()

app = BackendService(config)
