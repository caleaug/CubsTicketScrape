import requests, time
from bs4 import BeautifulSoup
import gspread
from google.oauth2.service_account import Credentials
import datetime

creds = Credentials.from_service_account_file("tickets-Cred.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
wks = client.open_by_key("1jD9KDi1VwgWO9cZ674cPUrZu0JnyV32RrD3eQKuBGIQ")
wks = wks.worksheets()[1]

def GetHTML(url):
  req = requests.get(url, headers={"Content-Type":"text"})
  soup = BeautifulSoup(req.content, 'html.parser')
  return soup

def getPrice(url):
    soup = GetHTML(url)

    try:
        t = str(soup).split('priceWithFees":"$')
        return(t[1].split('"')[0])
    except:
        print(soup)
        try:
            print(str(soup).split('priceWithFees":"$'))
        except:
            return "NA"
        return "NA"

def GetInfo(url):
    soup = GetHTML(url)
    s1 = str(soup).split('"formattedEventDateTime":')
    dateTime = s1[1].split('","')[0].replace('"',"")

    date = url.split("tickets-")[1].split("/")[0].split("-")    
    date1 = date[0] + "/" + date[1]
   
    ans = datetime.date(int(date[2]), int(date[0]), int(date[1]))
    day = ans.strftime("%a")


    t = str(soup).split('priceWithFees":"$')
    price = (t[1].split('"')[0])
    return(dateTime,date1,day,price)

def UpdateCell(x,y, val):
  wks.update_cell(y,x, val)

def UpdateAll():
    urlext = "/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seatTypes=&listingQty=&estimatedFees=true"
    y = 1
    for link in wks.col_values(5):
        if link:
            t0 = time.time()
            info = GetInfo(link+urlext)
            t1 = time.time()
            if t0+4>t1: time.sleep((t0+4)-t1)
            UpdateCell(1,y,info[0])
            UpdateCell(2,y,info[1])
            UpdateCell(3,y,info[2])
            UpdateCell(4,y,info[3])
        y+=1

def UpdatePrice():       
    urlext = "/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seatTypes=&listingQty=&estimatedFees=true"
    y = 1
    for link in wks.col_values(5):
        if link:
            price = getPrice(link+urlext)
            UpdateCell(4,y,price)
        y+=1

t = time.time()
UpdatePrice()
print(time.time()- t)
