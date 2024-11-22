import gspread, time
from google.oauth2.service_account import Credentials

p = "C:\\Users\\kingc\\OneDrive\\Documents\\Code\\TicketScrape\\tickets-Cred.json"

creds = Credentials.from_service_account_file(p , scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
sheets = client.open_by_key("1jD9KDi1VwgWO9cZ674cPUrZu0JnyV32RrD3eQKuBGIQ")
wksMain = sheets.get_worksheet_by_id(0) #main #sheets.worksheets()
wksKeys = sheets.get_worksheet_by_id(1432966988)

print(sheets.worksheets())
#wksMain.update_cell(14,14, time.asctime())

while True:
  wksMain.update_cell(14,14, time.asctime())
  time.sleep(1.1)
