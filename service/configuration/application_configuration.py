import os

from service.configuration.database_configuration import DatabaseConfiguration
from service.configuration.mysql_scoped_session_factory import MySQLScopedSessionFactory
from service.data.user_repository import UserRepository
from service.handlers.user_handler import UserHandler


class Configuration:
    def __init__(self):
        self.db = DatabaseConfiguration(host=os.getenv('DB_HOST'),
                                        port=os.getenv('DB_PORT', 3306),
                                        user=os.getenv('DB_USER', 'root'),
                                        password=os.getenv('DB_PASSWORD'),
                                        engine=os.getenv('DB_ENGINE'),
                                        db_name=os.getenv('DB_NAME')
                                        )

        self.db_session = MySQLScopedSessionFactory(self.db.connection_string()).create_session()

        self.user_repository = UserRepository(self.db_session)
        self.user_handler = UserHandler(self.user_repository)
