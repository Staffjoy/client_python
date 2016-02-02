from .resource import Resource
from .resources.organization import Organization
from .resources.cron import Cron
from .resources.user import User


class Client(Resource):
    def get_organizations(self, limit=25, offset=0):
        return Organization.get_all(parent=self, limit=limit, offset=offset)

    def get_organization(self, id):
        return Organization.get(parent=self, id=id)

    def create_organization(self, **kwargs):
        return Organization.create(parent=self, **kwargs)

    def cron(self):
        """Internal only - cron job manual timer"""
        return Cron.get_all(parent=self)

    def get_users(self, limit=25, offset=0, **kwargs):

        # Some supported filters: filterbyUsername, filterByEmail
        return User.get_all(parent=self, limit=limit, offset=offset, **kwargs)

    def get_user(self, id):
        return User.get(parent=self, id=id)
