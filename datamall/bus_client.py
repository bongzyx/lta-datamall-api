from .client import Client


class BusClient(Client):
    def get_arrivals(self, bus_stop_code):
        endpoint = f"BusArrivalv2?BusStopCode={bus_stop_code}"
        return self._make_request(endpoint)
