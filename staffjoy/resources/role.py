from ..resource import Resource
from .worker import Worker
from .schedule import Schedule


class Role(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}"
    ID_NAME = "role_id"

    def get_workers(self):
        return Worker.get_all(parent=self)

    def get_worker(self, id=id):
        return Worker.get(parent=self, id=id)

    def create_worker(self, **kwargs):
        return Worker.create(parent=self, **kwargs)

    def get_schedules(self, **kwargs):
        return Schedule.get_all(parent=self)

    def get_schedule(self, id):
        return Schedule.get(parent=self, id=id)
