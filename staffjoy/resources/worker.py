from ..resource import Resource


class Worker(Resource):
    """Organization administrators"""
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/users/{user_id}"
    ID_NAME = "user_id"
