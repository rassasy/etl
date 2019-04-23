from models import Headers

RESTAURANT_SET = set()

def validate(restaurant):
    errors = []

    errors.append(validate_name(restaurant.name))
    errors.append(validate_city(restaurant.city))
    errors.append(validate_state(restaurant.state))
    errors.append(validate_featured_on(restaurant.featured_on))
    errors.append(validate_cuisine(restaurant.cuisine))
    errors.append(validate_street_address(restaurant.street_address))
    errors.append(validate_country(restaurant.country))
    errors.append(validate_visited(restaurant.visited))
    errors.append(validate_keywords(restaurant.keywords))
    errors.append(validate_website(restaurant.website))
    errors.append(validate_yelp_site(restaurant.yelp_site))
    errors.append(is_unique(restaurant))

    filtered_list = list(filter(None, errors))

    if filtered_list:
        print_error(restaurant, filtered_list)
        return False
    
    RESTAURANT_SET.add(restaurant)
    return True


def validate_name(name) -> dict:
    return is_required(Headers.NAME, name)

def validate_city(city) -> dict:
    return is_required(Headers.CITY, city)
    ##TODO validate is a city

def validate_state(state) -> dict:
    return is_required(Headers.STATE, state)
    ##TODO validate is a state (conditional logic if it is international)

def validate_featured_on(featured_on) -> dict:
    return is_required(Headers.FEATURED_ON, featured_on)
    ##TODO validate known shows

def validate_cuisine(cuisine) -> dict:
    return is_required(Headers.CUISINE, cuisine)

def validate_street_address(address) -> dict:
    return is_required(Headers.STREET_ADDRESS, address)

def validate_country(country) -> dict:
    return is_required(Headers.COUNTRY, country)
    ##TODO validate is country

def validate_visited(visited) -> dict:
    return {}

def validate_keywords(keywords) -> dict:
    return is_array(Headers.KEYWORDS, keywords)

def validate_website(website) -> dict:
    return generate_field_error(Headers.WEBSITE, website, f"Field '{Headers.WEBSITE.name}' should not be a Yelp website") if "yelp.com" in website else {}

def validate_yelp_site(yelp_site) -> dict:
    return is_required(Headers.YELP_SITE, yelp_site)

def is_unique(restaurant):
    return generate_error(restaurant, "Restaurant must be a unique entry!") if restaurant in RESTAURANT_SET else {}
        
def is_required(header, value) -> dict:
    return generate_field_error(header, value, f"Field '{header.name}' must not be empty") if not value else {}

def is_array(header, value) -> dict:
    return generate_field_error(header, value, f"Field '{header.name}' must be an list") if not isinstance(value, list) else {}

def print_error(restaurant, errors) -> dict:
    print({
        "name": restaurant.name,
        "errors": errors
    })

def generate_error(restaurant, error) -> dict:
    return {
        "name": restaurant.name,
        "error": error
    }
def generate_field_error(header, value, error) -> dict:
    return {
        "field": header.name,
        "value": value,
        "error": error
    }
    