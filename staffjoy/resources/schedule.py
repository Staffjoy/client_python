from ..resource import Resource
from .availability import Availability
from .shift import Shift
from .schedule_message import ScheduleMessage


class Schedule(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/schedules/{schedule_id}"
    ID_NAME = "schedule_id"

    def get_availabilities(self, **kwargs):
        return Availability.get_all(parent=self, **kwargs)

    def get_availability(self, id):
        """ Get a worker's availability for a given week"""
        return Availability.get(parent=self, id=id)

    def create_availability(self, **kwargs):
        return Availability.create(parent=self, **kwargs)

    def get_shifts(self, **kwargs):
        return Shift.get(parent=self, **kwargs)

    def get_shift(self, id):
        return Shift.get(parent=self, id=id)

    def create_shift(self, **kwargs):
        return Shift.create(parent=self, **kwargs)

    def get_schedule_messages(self, **kwargs):
        return ScheduleMessage.get_all(parent=self, **kwargs)

    def get_schedule_message(self, id):
        return ScheduleMessage.get(parent=self, id=id)

    def create_schedule_message(self, **kwargs):
        return ScheduleMessage.create(parent=self, **kwargs)
