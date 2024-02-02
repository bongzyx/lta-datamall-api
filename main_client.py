from dotenv import dotenv_values
from datamall import BusClient

lta_env = dotenv_values(".env")
LTA_ACCOUNT_KEY = lta_env.get("LTA_ACCOUNT_KEY")


bus_stop = BusClient(LTA_ACCOUNT_KEY)
print(bus_stop.get_arrivals("46009"))
