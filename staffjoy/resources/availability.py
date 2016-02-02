from ..resource import Resource


class Availability(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/schedules/{schedule_id}/availabilities/{user_id}"
    ID_NAME = "user_id"
