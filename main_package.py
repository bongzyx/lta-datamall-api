from dotenv import dotenv_values
import datamall

lta_env = dotenv_values(".env")
LTA_ACCOUNT_KEY = lta_env.get("LTA_ACCOUNT_KEY")


lta = datamall.API(LTA_ACCOUNT_KEY)


bus_stops = lta.bus.get_bus_stops()
print(len(bus_stops))

bus_routes = lta.bus.get_bus_routes()
print(len(bus_stops))

bus_services = lta.bus.get_bus_services()
print(len(bus_stops))

bus_arrivals = lta.bus.get_arrivals("46009")
print(bus_arrivals)
