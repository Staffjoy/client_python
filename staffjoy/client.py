import logging

from .config import config


class Client:
    def __init__(self, key="", env="prod"):
        self.key = key

        self.config = config = config.get(env, "prod")
        self.logger = logging.getLogger()
        self.logger.setLevel(self.config.LOG_LEVEL)

        # These should be overridden by child classes
        self.path = ""  # URL path added to base, including route variables
        self.data = {}  # Data from the read method
        self.route = {}  # Route variables

        # TODO - get the self info?

    def get_organizations(self):
        pass

    def get_organization(self, id):
        pass

    def get_users(self,
                  limit=25,
                  offset=0,
                  filterByUsername=None,
                  filterByEmail=None):
        pass

    def get_user(self, id):
        pass