import uuid


class Tag(object):

    def __init__(self, value):
        self.id = uuid.uuid4()
        self.name = value

    def toNeo4j(self, session, parent_id):
        session.run(f'''MATCH (restaurant:Restaurant {{ id: \"{parent_id}\" }}) 
                        MERGE (tag:Tag {{ name:  \"{self.name}\" }})
                        ON CREATE SET tag.id = \"{self.id}\"
                        CREATE (restaurant)-[:TAGGED_WITH]->(tag)''')