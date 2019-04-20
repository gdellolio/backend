class DBSessionManager:
    def __init__(self, session):
        self._session = session

    def process_resource(self, req, resp, resource, params):
        resource.session = self._session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            if not req_succeeded:
                resource.session.rollback()
            self._session.remove()
