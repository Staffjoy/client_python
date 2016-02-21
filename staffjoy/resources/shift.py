from ..resource import Resource
from .shift_eligible_workers import ShiftEligibleWorker


class Shift(Resource):
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/shifts/{shift_id}"
    ID_NAME = "shift_id"

    def get_eligible_workers(self, **kwargs):
        return ShiftEligibleWorker.get_all(self, **kwargs)
