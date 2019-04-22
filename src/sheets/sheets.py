from oauth2client.service_account import ServiceAccountCredentials
import gspread


def init():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('.secrets/decrypted/sheets-credentials.json', scope)

    gc = gspread.authorize(credentials)

    worksheet = gc.open('Food Files').worksheet('Development')
    values = worksheet.get_all_values()
    header_values = list(filter(None, values.pop(0)))

    return header_values, values

def get_header_values():
    return header_values

def get_values():
    return values

header_values, values = init()