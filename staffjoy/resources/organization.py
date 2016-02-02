from ..resource import Resource


class Organization(Resource):
    PATH = "organizations/{organization_id}"
    ID_NAME = "organization_id"
