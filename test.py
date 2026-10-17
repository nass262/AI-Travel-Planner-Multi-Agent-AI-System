#from tools.tavily_tool import tavily_search

from tools.flight_tool import search_flights
#from backend import run_travel_agent

#res = tavily_search("Best hotels in Morocco")
#print(res)

res = search_flights("Plan a 7 days Pris trip from Morocco")
print(res)