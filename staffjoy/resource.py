import requests
from copy import copy

from .config import config_from_env
from .exceptions import UnauthorizedException, NotFoundException, BadRequestException


class Resource:
    PATH = ""  # URL path added to base, including route variables
    ID_NAME = None  # What is this ID called in the route of children?
    META_ENVELOPES = []  # Metadata keys for what to unpack from response
    ENVELOPE = "data"  # We "envelope" response data in the "data" section
    TRUTHY_CODES = [requests.codes.ok, requests.codes.created,
                    requests.codes.no_content, requests.codes.accepted]

    def __init__(self,
                 key="",
                 config=None,
                 env="prod",
                 logger=None,
                 data={},
                 route={},
                 meta={}):
        """Initialize the resource"""
        self.key = key

        self.config = config or config_from_env.get(env, "prod")
        if logger is None:
            self.logger = logging.getLogger()
            self.logger.setLevel(self.config.LOG_LEVEL)

        # These should be overridden by child classes
        self.data = data  # Data from the read method
        self.route = route  # Route variables
        self.meta = meta  # Meta data

    @classmethod
    def get(cls, parent=None, id=None, data=None):
        """Inherit info from parent and return new object"""
        # TODO - allow fetching of parent based on child?

        if parent is not None:
            route = copy(parent.route)
        else:
            route = {}

        if id is not None and cls.ID_NAME is not None:
            route[cls.ID_NAME] = id

        obj = cls(key=parent.key, route=route, logger=parent.logger)

        if data:
            # This is used in "get all" queries
            obj.data = data
        else:
            obj.fetch()

        return obj

    @classmethod
    def get_all(cls, parent=None, **params):

        if cls.ID_NAME is not None:
            # Empty string triggers "get all resources"
            route[cls.ID_NAME] = ""

        base_obj = cls(key=parent.key, route=route, logger=parent.logger)
        """Perform a read request against the resource"""
        base_obj.logger.debug("Fetching all {}".format(base_obj._url()))
        r = requests.get(self._url(), auth=(base_obj.key, None), params=params)
        base_obj.logger.debug("Response {}".format(r))

        if r.status_code not in self.TRUTHY_CODES:
            return self._handle_request_exception(r)

        response = r.json()
        objects_data = response.get(base_obj.ENVELOPE, [])

        return_objects = []
        for data in objects_data:
            # Note that this approach does not get meta data
            return_objects.append(cls.get(parent=parent,
                                          id=data.get(self.ID_NAME),
                                          data=data))

        return return_objects

    def _url(self):
        """Get the URL for the resource"""
        return self.config.BASE + self.PATH.format(**self.route)

    def _handle_request_exception(self, request):
        """Raise the proper exception based on the response"""
        try:
            data = request.json()
        except:
            data = None

        code = request.status_code
        if code is requests.codes.bad:
            raise BadRequestException(response=data)

        if code is requests.code.unauthorized:
            raise UnauthorizedException(response=data)

        if code is requests.code.not_found:
            raise UnauthorizedException(response=data)

        # Generic error fallback
        request.raise_for_exception()

    def fetch(self):
        """Perform a read request against the resource"""
        self.logger.debug("Fetching {}".format(self._url()))
        r = requests.get(self._url(), auth=(self.key, None))
        self.logger.debug("Fetch response {}".format(r))
        if r.status_code not in self.TRUTHY_CODES:
            return self._handle_request_exception(r)

        response = r.json()
        self.data = response.get("data", {})

        # Move to separate function so it can be overrridden
        self._process_meta(response)

        self.logger.debug("Fetched {}")

    def _process_meta(self, response):
        """Process additional data sent in response"""
        for key in self.META_ENVELOPES:
            self.meta[key] = response.get(key)

    def delete(self):
        """Delete the object"""

        self.logger.debug("Calling delete to {}".format(self._url()))
        r = requests.get(self._url(), auth=(self.key, None))
        self.logger.debug("Delete response {}".format(r))
        if r.status_code not in self.TRUTHY_CODES:
            return self._handle_request_exception(r)
        self.logger.debug("Deleted {}".format(self))

    def patch(self, **kwargs):
        """Change attributes of the item"""
        self.logger.debug("Calling patch to {}".format(self._url()))
        r = requests.get(self._url(), auth=(self.key, None))
        self.logger.debug("Patch response {}".format(r))
        if r.status_code not in self.TRUTHY_CODES:
            return self._handle_request_exception(r)

        self.logger.debug("Patched {}".format(self))

        # Refetch for safety. We could modify based on response,
        # but I'm afraid of some edge cases and marshal functions.
        self.fetch()

    @classmethod
    def create(cls, parent=None, **kwargs):
        if parent is None:
            return cls()

        route = copy(parent.route)
        if id is not None and cls.ID_NAME is not None:
            route[cls.ID_NAME] = id

        obj = cls(key=parent.key, route=route, logger=parent.logger)

        obj.fetch()
        return obj
        pass

    def __str__(self):
        return "{} id {}".format(self.__class__.__name__,
                                 self.route.get(self.ID_NAME))
