from TicketInit import *

def GetPrice(key, driver):
  i = 0
  while i<3:
    try:
      driver.get("https://www.ticketmaster.com/event/" +key)
      try: driver.find_element(By.XPATH, '//*[@id="modalContent"]/div[3]/div/button/span/span').click()
      except: pass
      driver.find_element(By.XPATH, '//*[@id="filter-bar-quantity"]/option[1]').click()
      driver.find_element(By.XPATH, '//*[@id="edp-quantity-filter-button"]').click()
      time.sleep(0.5)
      driver.find_element(By.XPATH, '/html/body/div[2]/div/div[6]/div/div[2]/section/div[1]/div[2]/div[2]/div[1]/div/div/form/div[3]/div/button/div/div[2]/div').click()
      driver.find_element(By.XPATH, '//*[@id="ismqp-template-left"]/div[2]/div[2]/div[2]/div/button[2]').click()

      elem = driver.find_element(By.XPATH, '//*[@id="edp-quantity-filter-button"]')
      ac = ActionChains(driver)
      ac.move_to_element(elem).move_by_offset(-850,30).click().perform()
      time.sleep(0.5)
      page = BeautifulSoup(driver.page_source, "html.parser")
      price = str(page).split('data-price="$')[1].split('"')[0]

      return round(float(price)+3.95)
    except Exception as e:
      i+=1
  return "NA"

##url = "https://www.ticketmaster.com/event/Z7r9jZ1AdPfJb"
##driver = uc.Chrome()
##driver.get(url)
##
##elem = driver.find_element(By.XPATH, '//*[@id="edp-quantity-filter-button"]')
##ac = ActionChains(driver)
##ac.move_to_element(elem).move_by_offset(-850,30).click().perform()
##price = str(page).split('data-price="$')[1].split(".")[0]


def UpdateTicketMaster():
  t = time.time()

  driver = uc.Chrome()
  Keys = FindKeys("TicketMaster")
  y=1
  dates = wksMain.col_values(2)
  for d in dates:
    if d in Keys.keys() and DateValid(d):
      price = GetPrice(Keys[d], driver)
      UpdateCell(y, FindColumn("TicketMaster") ,price)
    y+=1
  driver.close()
  print("TickPick:", round(time.time()-t,2),round((time.time()-t)/60,2))

driver = uc.Chrome()
Keys = FindKeys("TicketMaster")
