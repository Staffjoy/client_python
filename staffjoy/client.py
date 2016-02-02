from .resource import Resource
from .resources.organization import Organization


class Client(Resource):
    def get_organizations(self):
        return Organization.get_all(parent=self)

    def get_organization(self, id):
        return Organization.get(parent=self, id=id)

    """
    def get_users(self,
                  limit=25,
                  offset=0,
                  filterByUsername=None,
                  filterByEmail=None):



    def get_user(self, id):
        pass
    """