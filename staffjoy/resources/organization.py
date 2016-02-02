from ..resource import Resource
from .location import Location


class Organization(Resource):
    PATH = "organizations/{organization_id}"
    ID_NAME = "organization_id"

    def get_locations(self):
        return Location.get_all(parent=self)

    def get_location(self, id):
        return Location.get(parent=self, id=id)

    def create_location(self, **kwargs):
        return Location.create(parent=self, **kwargs)
