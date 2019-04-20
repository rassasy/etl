import gspread
from oauth2client.service_account import ServiceAccountCredentials


def init():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('.secrets/decrypted/sheets-credentials.json', scope)

    gc = gspread.authorize(credentials)

    sheet = gc.open('Food Files')
    restaurants = sheet.worksheet('Development').get_all_values()
    header_values = list(filter(None, restaurants.pop(0)))
    headers = {}
    
    for name in header_values:
        headers[name.strip()] = header_values.index(name)

    return headers, restaurants

HEADERS, RESTAURANTS = init()