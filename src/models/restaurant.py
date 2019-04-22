from . import Headers
from . import ValidationException

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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

    # @property
    # def city(self):
    #     return self._city

    # @city.setter
    # def city(self, city):
    #     self._city = city

    # @property
    # def state(self):
    #     return self._state

    # @state.setter
    # def state(self, state):
    #     self._state = state

    # @property
    # def featured_on(self):
    #     return self._featured_on
    
    # @featured_on.setter
    # def featured_on(self, featured_on):
    #     self._featured_on = featured_on

    # @property
    # def cuisine(self):
    #     return self._cuisine

    # @cuisine.setter
    # def cuisine(self, cuisine):
    #     self._cuisine = cuisine

    # @property
    # def description(self):
    #     return self._description

    # @description.setter
    # def description(self, description):
    #     self._description = description

    # @property
    # def notes(self):
    #     return self._notes

    # @notes.setter
    # def notes(self, notes):
    #     self._notes = notes
    
    # @property
    # def street_address(self):
    #     return self._street_address

    # @street_address.setter
    # def street_address(self, street_address):
    #     self._street_address = street_address

    # @property
    # def country(self):
    #     return self._country

    # @country.setter
    # def country(self, country):
    #     self._country = country
    
    # @property
    # def visited(self):
    #     return self._visited

    # @visited.setter
    # def visited(self, visited):
    #     self._visited = visited

    # @property
    # def keywords(self):
    #     return self._keywords

    # @keywords.setter
    # def keywords(self, keywords):
    #     self._keywords = keywords

    # @property
    # def yelp_rating(self):
    #     return self._yelp_rating

    # @yelp_rating.setter
    # def yelp_rating(self, yelp_rating):
    #     self._yelp_rating = yelp_rating

    # @property
    # def website(self):
    #     return self._website

    # @website.setter
    # def website(self, website):
    #     self._website = website

    # @property
    # def yelp_site(self):
    #     return self._yelp_site

    # @yelp_site.setter
    # def yelp_site(self, yelp_site):
    #     self._yelp_site = yelp_site