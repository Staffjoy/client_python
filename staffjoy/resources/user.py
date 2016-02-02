from ..resource import Resource


class User(Resource):
    PATH = "users/{user_id}"
    ID_NAME = "user_id"
