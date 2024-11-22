from TicketInit import *

def GetPrice1(key):
  url = ('https://www.tickpick.com/buy-chicago-cubs-vs-tickets-wrigley-field/' + str(key)
    + "?sections=stars:any%7Cinclude:GA%20Bleachers%7Cexclude:all&qty=1-false")
  driver = uc.Chrome()
  driver.get(url)

  price, t0, t = None, time.time(), 0
  while not price:
    try:
      page = BeautifulSoup(driver.page_source, "html.parser")
      p1 = page.find("div", {"id": "listingContainer"})
      price = p1.div.b.text.replace("$","")
      time.time()
    except:
      time.sleep(0.1)
    if t0 + 5<time.time():
      driver.close() 
      driver = uc.Chrome()
      driver.get(url)
      t0 = time.time()
      t+=1
    if t == 4:
      driver.close()
      return "NA"

  driver.close()
  return price

def UpdateTickPick():
  Keys = FindKeys("TickPick")
  t = time.time()
  y=1
  dates = wksMain.col_values(2)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      price = GetPrice1(Keys[d])
      UpdateCell(y, FindColumn("TickPick") ,price)
    y+=1

  print("TickPick:", round(time.time()-t,2),round((time.time()-t)/60,2))


