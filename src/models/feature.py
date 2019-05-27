from .feature_type import FeatureType

import uuid 


class Feature(object):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.type = FeatureType.SHOW if "Personal" not in name else FeatureType.PERSON

    def toNeo4j(self, session, parent_id):
        session.run(f'''MATCH (restaurant:Restaurant {{ id: \"{parent_id}\" }}) 
                        MERGE (feature:Feature {{ name: \"{self.name}\" }})
                        ON CREATE SET feature.id = \"{self.id}\"
                        CREATE (restaurant)-[:FEATURED_BY]->(feature)''')
                       


