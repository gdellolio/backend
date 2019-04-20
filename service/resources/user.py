import json


class Collection:
    def __init__(self, user_handler):
        self._user_handler = user_handler

    def on_get(self, req, resp):
        doc = self._user_handler.get_users()

        resp.body = json.dumps(doc, ensure_ascii=False)


class Item:
    def __init__(self, user_handler):
        self._user_handler = user_handler

    def on_get(self, req, resp, user_id):
        doc = self._user_handler.get_user_by_id(user_id)

        resp.body = json.dumps(doc, ensure_ascii=False)
