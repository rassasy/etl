from .feature_type import FeatureType

import uuid 


class Feature(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.type = FeatureType.SHOW if "Personal" not in name else FeatureType.PERSON


