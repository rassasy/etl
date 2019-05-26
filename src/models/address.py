import uuid


class Address(object):

    def __init__(self, value):
        self.id = uuid.uuid4()
        self.value = value