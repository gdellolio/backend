from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class MySQLScopedSessionFactory:
    def __init__(self, connection_url):
        self._connection_url = connection_url

    def create_session(self):
        session_factory = sessionmaker(bind=self._create_engine())

        session = scoped_session(session_factory)

        return session

    def _create_engine(self):
        engine = create_engine(self._connection_url)

        return engine
