from ..resource import Resource


class Location(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}"
    ID_NAME = "location_id"
