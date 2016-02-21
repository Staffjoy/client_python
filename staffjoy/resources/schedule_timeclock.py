from ..resource import Resource


class ScheduleTimeclock(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/schedules/{schedule_id}/timeclocks/"
