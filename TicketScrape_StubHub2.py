from TicketInit import *

def GetPrice(key,driver):
  url = ("https://www.stubhub.com/chicago-cubs-chicago-tickets/event/"+str(key)+
  "/?quantity=1&sections=1441865&ticketClasses=4380&rows=&seatTypes=&listingQty=&estimatedFees=true")
  driver.get(url)
  page = BeautifulSoup(driver.page_source, "html.parser")

  p1 = str(page).split('data-price="$')[1]
  return p1.split('"')[0]

def UpdateStubHub():
  Keys = FindKeys("StubHub")
  driver = webdriver.Chrome(service=s, options=options)
  t = time.time()
  y=1
  dates = wksMain.col_values(2)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      price = GetPrice(Keys[d],driver)
      UpdateCell(y, FindColumn("StubHub") ,price)
    y+=1

  driver.close()
  print("StubHub:", round(time.time()-t,2),round((time.time()-t)/60,2))



