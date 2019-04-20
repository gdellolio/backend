import falcon

from service.middleware.db_session_manager import DBSessionManager
from service.resources.user import Item, Collection


class BackendService(falcon.API):
    def __init__(self, configuration):
        super(BackendService, self).__init__(middleware=DBSessionManager(configuration.db_session))

        self.add_route('/user/{user_id}', Item(configuration.user_handler))
        self.add_route('/user', Collection(configuration.user_handler))
