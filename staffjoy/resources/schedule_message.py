from ..resource import Resource


class ScheduleMessage(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/schedules/{schedule_id}/messages/{message_id}"
    ID_NAME = "message_id"
