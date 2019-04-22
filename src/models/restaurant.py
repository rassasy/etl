from . import Headers

import json


class Restaurant(object):

    def __init__(self, data):
        self.name = data[Headers.NAME.value]
        self.city = data[Headers.CITY.value]
        self.state = data[Headers.STATE.value]
        self.featured_on = data[Headers.FEATURED_ON.value].splitlines()
        self.cuisine = data[Headers.CUISINE.value].splitlines()
        self.description = data[Headers.DESCRIPTION.value]
        self.notes = data[Headers.NOTES.value]
        self.street_address = data[Headers.STREET_ADDRESS.value]
        self.country = data[Headers.COUNTRY.value]
        self.visited = data[Headers.VISITED.value]
        self.keywords = data[Headers.KEYWORDS.value].splitlines()
        self.yelp_rating = data[Headers.YELP_RATING.value]
        self.website = data[Headers.WEBSITE.value]
        self.yelp_site = data[Headers.YELP_SITE.value]
    
    def __str__(self):
        return f'''Restaurant
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
        