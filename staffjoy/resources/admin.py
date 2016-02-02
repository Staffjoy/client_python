from ..resource import Resource


class Admin(Resource):
    """Organization administrators"""
    PATH = "organizations/{organization_id}/users/{user_id}"
    ID_NAME = "user_id"
