from . import Location, Feature, Headers
from .tag import Tag

import json
import uuid


class Restaurant(object):

    def __init__(self, data):
        self.id = str(uuid.uuid4())
        self.name = data[Headers.NAME.value]
        self.city = data[Headers.CITY.value]
        self.state = data[Headers.STATE.value]
        self.featured_on = list(map(lambda name : Feature(name), data[Headers.FEATURED_ON.value].splitlines()))
        self.cuisine = data[Headers.CUISINE.value].splitlines()
        self.description = data[Headers.DESCRIPTION.value]
        self.notes = data[Headers.NOTES.value]
        self.street_address = list(map(lambda value: Location(self.city, self.state, value), data[Headers.STREET_ADDRESS.value].splitlines()))
        self.country = data[Headers.COUNTRY.value]
        self.visited = data[Headers.VISITED.value]
        self.keywords = list(map(lambda keyword: Tag(keyword), data[Headers.KEYWORDS.value].splitlines()))
        self.yelp_rating = data[Headers.YELP_RATING.value]
        self.website = data[Headers.WEBSITE.value]
        self.yelp_site = data[Headers.YELP_SITE.value]
    
    def __str__(self):
        return f'''Restaurant
        ID: {self.id}
        Name: {self.name}
        City: {self.city}
        State: {self.state}
        Featured On: {self.featured_on}
        Cuisine: {self.cuisine}
        Description: {self.description}
        Notes: {self.notes}
        Street Address: {self.street_address}
        Country: {self.country}
        Visited: {self.visited}
        Keywords: {self.keywords}
        Yelp Rating: {self.yelp_rating}
        Website: {self.website}
        Yelp Site: {self.yelp_site}
        '''

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(('name', self.name))

    def toSQL(self, conn):
        conn.execute('INSERT INTO rassasy.restaurant_detail VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
            self.id, self.name, self.city, self.state, self.description, self.notes, self.country, 
            self.visited, self.website, self.yelp_site
        ))

        for feature in self.featured_on:
            conn.execute('INSERT INTO rassasy.feature VALUES (%s, %s, %s)', (str(uuid.uuid4()), feature.name, feature.type.name))
        
        for location in self.street_address:
            locationId = str(uuid.uuid4())
            conn.execute('INSERT INTO rassasy.location VALUES (%s, %s)', (locationId, location.value))
            conn.execute('INSERT INTO rassasy.located VALUES (%s, %s, %s)', (str(uuid.uuid4()), self.id, locationId))

        for tag in self.keywords:
            tagId = str(uuid.uuid4())
            conn.execute('INSERT INTO rassasy.tag VALUES (%s, %s)', (tagId, tag.name))
            conn.execute('INSERT INTO rassasy.tagged VALUES (%s, %s, %s)', (str(uuid.uuid4()), self.id, tagId))

    def toNeo4j(self, session):
        session.run(f"CREATE (:Restaurant {{ id: \"{self.id}\" }})")

        for feature in self.featured_on:
            feature.toNeo4j(session, self.id)

        for location in self.street_address:
            location.toNeo4j(session, self.id)

        for tag in self.keywords:
            tag.toNeo4j(session, self.id)
