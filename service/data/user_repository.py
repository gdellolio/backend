from service.data.models.user import User


class UserRepository:
    def __init__(self, db_session):
        self._db_session = db_session

    def get_user_by_id(self, user_id):
        user = self._db_session.query(User).filter(User.id == user_id).first()

        return user

    def get_users(self):
        users = self._db_session.query(User).all()

        return users
