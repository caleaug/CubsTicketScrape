from TicketInit import *

def OneTicket(driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span/span/div/span/button').click()
    driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span/span/div[2]/div/div/button[2]/div/span').click()

def IncludeFees(driver):
  driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/button[1]').click()
  try:    driver.find_element(By.XPATH, '/html/body/div[12]/div/div/form/div[1]/div[2]/label/div[1]/div[2]/input').click()
  except: driver.find_element(By.XPATH, '/html/body/div[11]/div/div/form/div[1]/div[2]/label/div[1]/div[2]/input').click()
  driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/button[1]').click()

def GetPrice(key, driver):
  driver.get("https://seatgeek.com/chicago-cubs-tickets/a/mlb/" + key)

  page = BeautifulSoup(driver.page_source, "html.parser")
  if "captcha-delivery" in str(page):
    print("Capta")
    driver = Capta(driver)
    driver.get("https://seatgeek.com/chicago-cubs-tickets/a/mlb/" + key)

  for i in range(2):
    try:
      OneTicket(driver)

      elem = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/span[2]/span/header/div/nav[2]/div[2]/div/div/a[2]/p')
      ac = ActionChains(driver)
      ac.move_to_element(elem).move_by_offset(-380,180).click().perform()

      page = BeautifulSoup(driver.page_source, "html.parser")

      s2 = str(page).split('aria-label="Budweiser Bleachers GA')[1].split('$')[2]
      price = s2.split("<")[0]
      print(price, "incl. fees" in s2,"1" in s2.split('</p>')[0].split(">")[-1], s2.split('</p>')[0].split(">")[-1])
      return driver, price
    except Exception as e: pass
  print("NA")
  return driver, "NA"

def Capta(driver="na"):
  try: driver.close()
  except Exception as e: pass

  driver = uc.Chrome()
        
  Keys = FindKeys("SeatGeek")
  driver.get("https://seatgeek.com/chicago-cubs-tickets/a/mlb/" + Keys[list(Keys)[0]])

  time.sleep(20)
  IncludeFees(driver)
  return driver

def UpdateSeatGeek():
  driver = Capta()
  Keys = FindKeys("SeatGeek")
  t = time.time()

  y=1
  dates = wksMain.col_values(2)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      driver, price = GetPrice(Keys[d], driver)
      UpdateCell(y, FindColumn("SeatGeek") ,price)
      #time.sleep(1) #######
    y+=1
  driver.close()
  print("SeatGeek:", round(time.time()-t,2),round((time.time()-t)/60,2))


