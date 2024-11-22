import requests, time
from bs4 import BeautifulSoup
import gspread
from google.oauth2.service_account import Credentials

creds = Credentials.from_service_account_file("tickets-Cred.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
wks = client.open_by_key("1jD9KDi1VwgWO9cZ674cPUrZu0JnyV32RrD3eQKuBGIQ").sheet1

Keys = {
  "8/16" : 152171312,
  "8/17" : 152171302,
  "8/18" : 152171485,
  "8/20" : 152171487,
  "8/21" : 152171494,
  "8/22" : 152171490,
  "9/2" : 152171492,
  "9/3" : 152171496,
  "9/4" : 152171491,
  "9/6" : 152171488,
  "9/7" : 152171495,
  "9/8" : 152171489,
  "9/16" : 152171507,
  "9/17" : 152171511,
  "9/18" : 152171510,
  "9/19" : 152171509,
  "9/20" : 152171508,
  "9/21" : 152171516,
  "9/22" : 152171513,
  "9/27" : 152171514,
  "9/28" : 152171515,
  "9/29" : 152171512
  }

def GetHTML(url):
  req = requests.get(url, headers={"Content-Type":"text"})
  soup = BeautifulSoup(req.content, 'html.parser')
  return soup

def GetPrice(key):
  url = ("https://www.stubhub.com/chicago-cubs-chicago-tickets/event/"+str(key)+
  "/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seatTypes=&listingQty=&estimatedFees=true")
  soup = GetHTML(url)

  t = str(soup).split('priceWithFees":"$')
  return(t[1].split('"')[0])

def UpdateCell(x,y, val):
  wks.update_cell(x,y, val)

def UpdateStubHub():
  t = time.time()
  y=1
  dates = wks.col_values(2)
  for d in dates:
    if d in Keys.keys():
      price = GetPrice(Keys[d])
      UpdateCell(y,3,price)
    y+=1
  print("StubHub:", round(time.time()-t,2),round((time.time()-t)/60,2))



