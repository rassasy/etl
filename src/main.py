import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('.secrets/decrypted/sheets-credentials.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open('Food Files')
values = sheet.worksheet('Development').get_all_values()