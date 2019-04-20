from src.sheets import HEADERS

def test_headers():
    print(HEADERS)
    expected_headers = ['Name', 
                        'City', 
                        'State', 
                        'Featured On', 
                        'Cuisine', 
                        'Description', 
                        'Notes', 
                        'Street Address', 
                        'Country',
                        'Visited',
                        'Keywords',
                        'Yelp Rating',
                        'Website',
                        'Yelp']
    
    assert len(HEADERS) == len(expected_headers)

    for expected_header in expected_headers:
        print(f"EXPECTED: {expected_headers.index(expected_header)}")
        print(f"ACTUAL: {HEADERS[expected_header]}")
        assert expected_headers.index(expected_header) == HEADERS[expected_header]