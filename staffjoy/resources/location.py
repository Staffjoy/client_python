from ..resource import Resource
from .role import Role
from .manager import Manager


class Location(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}"
    ID_NAME = "location_id"

    def get_roles(self, **kwargs):
        return Role.get_all(parent=self, **kwargs)

    def get_role(self, id):
        return Role.get(parent=self, id=id)

    def create_role(self, **kwargs):
        return Role.create(parent=self, **kwargs)

    def get_managers(self, **kwargs):
        return Manager.get_all(parent=self, **kwargs)

    def get_manager(self, id):
        return Manager.get(parent=self, id=id)

    def create_manager(self, **kwargs):
        """Typically just pass email"""
        return Manager.create(parent=self, **kwargs)
