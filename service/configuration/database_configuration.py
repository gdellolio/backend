class DatabaseConfiguration:
    def __init__(self, host, port, user, password, engine, db_name):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._engine = engine
        self._db_name = db_name

    def connection_string(self):
        return f'{self._engine}://{self._user}:{self._password}@{self._host}:{self._port}/{self._db_name}'
