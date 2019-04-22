from src.sheets import get_header_values
from src.models import Headers

header_values = get_header_values()

def test_headers():
    for header in Headers:
        assert header.name.replace('_', ' ').lower() == header_values[header.value].lower()