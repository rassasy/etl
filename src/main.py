from client import insert_restaurants, insert_restaurant_links
from models import Headers, Restaurant
from sheets import get_values
from validation import validate


def parse_restaurants(data) -> []:
    restaurants = []

    for value in data:
        restaurant = Restaurant(value)
        if validate(restaurant):
            restaurants.append(restaurant)    
        
    return restaurants

data = get_values()
restaurants = parse_restaurants(data)

insert_restaurant_links(restaurants)