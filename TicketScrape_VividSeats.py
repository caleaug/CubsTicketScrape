from TicketInit import *

url= "https://www.ticketmaster.com/"

driver = webdriver.Chrome(service=s, options=options)
driver.get(url)

time.sleep(10)
page = BeautifulSoup(driver.page_source, "html.parser")
print(page)
