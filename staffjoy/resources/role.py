from ..resource import Resource


class Role(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}"
    ID_NAME = "role_id"
