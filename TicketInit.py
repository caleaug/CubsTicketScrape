import requests, time
from bs4 import BeautifulSoup
import gspread, datetime
from google.oauth2.service_account import Credentials

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains

Path = "C:\Program Files (x86)\chromedriver.exe"
s=Service(Path)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

credsPath = p = "C:\\Users\\kingc\\OneDrive\\Documents\\Code\\tickets-Cred.json"
creds = Credentials.from_service_account_file("credsPath", scopes=["https://www.googleapis.com/auth/spreadsheets"])
client = gspread.authorize(creds)
sheets = client.open_by_key("1jD9KDi1VwgWO9cZ674cPUrZu0JnyV32RrD3eQKuBGIQ")
wksMain = sheets.get_worksheet_by_id(0) #main #sheets.worksheets()
wksKeys = sheets.get_worksheet_by_id(1432966988)
wksCheapest = sheets.get_worksheet_by_id(855558548)


def UpdateCell(x,y, val):
  wksMain.update_cell(x,y, val)

def DateValid(date):
  if date:
    Cy = int(datetime.date.today().strftime("%y"))
    Cm = int(datetime.date.today().strftime("%m"))
    Cd = int(datetime.date.today().strftime("%d"))

    y = int(date.split("/")[2])
    m = int(date.split("/")[0])
    d = int(date.split("/")[1])
    if y > Cy: return True
    if Cy < y: return False
    if m > Cm: return True
    if m == Cm and d >= Cd: return True
  return False

def FindColumn(head, sheet = wksMain):
  headings = sheet.row_values(1)
  c=1
  for h in headings:
    if h == head: return c
    c+=1

def FindKeys(head):
  Keys = {}
  DateCol = wksKeys.col_values(FindColumn("Date", wksKeys))[1:]
  KeyCol = wksKeys.col_values(FindColumn(head, wksKeys))[1:]

  for d, k in zip(DateCol,KeyCol):Keys[d] = k
  return Keys

def UpdateCheapest():
  prices = {}
  DateCol = wksMain.col_values(FindColumn("Date"))[1:]
  CheapestCol = wksMain.col_values(FindColumn("Cheapest"))[1:]

  for d, c in zip(DateCol,CheapestCol):prices[d] = c

  FreeCol = len(wksCheapest.row_values(1)) + 1

  wksCheapest.update_cell(1,FreeCol, str(datetime.date.today().strftime("%m/%d"))+'\n'+"20"+datetime.date.today().strftime("%y"))
  Dates = wksCheapest.col_values(FindColumn("Date", wksCheapest))[1:]
  y = 2 
  for d in Dates:
    #print(d)
    if d in list(prices): wksCheapest.update_cell(y,FreeCol,prices[d])
    y+=1
    time.sleep(1)
  

  

