from dotenv import dotenv_values
import datamall

lta_env = dotenv_values(".env")
LTA_ACCOUNT_KEY = lta_env.get("LTA_ACCOUNT_KEY")


lta = datamall.API(LTA_ACCOUNT_KEY)
bus_stop = lta.bus.get_arrivals("47491")
# taxi_stand_info = lta.taxi.get_stand_info("123")
# train_alerts = lta.train.get_service_alerts()
print(bus_stop)
