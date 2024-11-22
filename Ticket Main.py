from TicketInit import *
from TicketScrape_StubHub2 import UpdateStubHub
from TicketScrape_GameTime import UpdateGameTime
from TicketScrape_TickPick import UpdateTickPick

t = time.time()
UpdateStubHub()
UpdateGameTime()
UpdateTickPick()
print("All:", round(time.time()-t,2),round((time.time()-t)/60,2))
