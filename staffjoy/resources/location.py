from ..resource import Resource
from .role import Role


class Location(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}"
    ID_NAME = "location_id"

    def get_roles(self):
        return Role.get_all(parent=self)

    def get_role(self, id):
        return Role.get(parent=self, id=id)

    def create_role(self, **kwargs):
        return Role.create(parent=self, **kwargs)
