class UserHandler:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def get_user_by_id(self, user_id):
        user = self._user_repository.get_user_by_id(user_id)

        return {'name': user.name, 'age': user.age}

    def get_users(self):
        users = self._user_repository.get_users()

        user_dict = []
        for user in users:
            user_dict.append({'name': user.name, 'age': user.age})

        return user_dict
