from ..resource import Resource


class MobiusTask(Resource):
    PATH = "/internal/tasking/mobius/{schedule_id}"
    ENVELOPE = None
