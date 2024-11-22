from TicketInit import *

def GetPrice(key, driver):
  driver.get("https://gametime.co/mlb-baseball/chicago-il-wrigley-field/events/" + key)
  page = BeautifulSoup(driver.page_source, "html.parser")
  
  s1 = str(page).split('style="top:')[1:]
  AvgX, AvgY = 0,0
  for s in s1:
    x = s.split("px;")[0].replace(" ","").replace("left:","")
    y = s.split("px;")[1].replace(" ","").replace("left:","")
    price = s.split('pin">')[1].split("<")[0]

    x, y = float(x), float(y)
    AvgX, AvgY = AvgX + x, AvgY + y
  
  AvgX, AvgY = AvgX/len(s1), AvgY/len(s1)

  for s in s1:
    x = s.split("px;")[0].replace(" ","").replace("left:","")
    y = s.split("px;")[1].replace(" ","").replace("left:","")
    price = s.split('pin">')[1].split("<")[0]         
    x, y = float(x), float(y)
    if x < AvgX/2 and y > AvgY:
      return price.replace("$","")

def UpdateGameTime():
  Keys = FindKeys("GameTime")
  driver = webdriver.Chrome(service=s, options=options)
  driver.get("https://gametime.co/mlb-baseball/chicago-il-wrigley-field/events/" + Keys[list(Keys)[0]])
  driver.find_element("id","CardId003").click()

  t = time.time()
  y=1
  dates = wksMain.col_values(2)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      price = GetPrice(Keys[d],driver)
      UpdateCell(y, FindColumn("GameTime") ,price)
    y+=1

  driver.close()
  print("GameTime:", round(time.time()-t,2),round((time.time()-t)/60,2))










