import uuid


class Tag(object):

    def __init__(self, value):
        self.id = uuid.uuid4()
        self.name = value