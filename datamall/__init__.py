from .bus_client import BusClient


class API:
    def __init__(self, api_key):
        self.bus = BusClient(api_key)
        # self.taxi = Taxi(api_key)
        # self.train = Train(api_key)
        # self.traffic = Traffic(api_key)
        # self.erp = ERP(api_key)
