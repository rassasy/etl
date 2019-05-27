import uuid


class Location(object):

    def __init__(self, city, state, street_address):
        self.id = uuid.uuid4()
        self.city = city
        self.state = state
        self.street_address = street_address

    def toNeo4j(self, session, parent_id):
        session.run(f'''MATCH (restaurant:Restaurant {{ id: \"{parent_id}\" }})
                        MERGE (location:Location {{
                            city: \"{self.city}\",
                            state: \"{self.state}\"
                        }})
                        ON CREATE SET location.id = \"{self.id}\"
                        CREATE (restaurant)-[:LOCATED_AT {{
                            address: \"{self.street_address}\"
                        }}]->(location)''')

