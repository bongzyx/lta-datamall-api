from .client import Client
from .utils import calculate_time
import re


class BusClient(Client):
    def get_arrivals(self, bus_stop_code):
        if re.match(r"\b\d{5}\b", str(bus_stop_code)):
            endpoint = f"BusArrivalv2?BusStopCode={bus_stop_code}"
            arrivals = self.handle_arrivals(self._make_request(endpoint))

            return arrivals
        return None

    def get_bus_stops(self):
        bus_stops_data = self._make_loop_requests("BusStops")

        self.save_to_file(bus_stops_data, "bus_stops")

        return bus_stops_data

    def get_bus_routes(self):
        bus_routes_data = self._make_loop_requests("BusRoutes")

        self.save_to_file(bus_routes_data, "bus_routes")

        return bus_routes_data

    def get_bus_services(self):
        bus_services_data = self._make_loop_requests("BusServices")

        self.save_to_file(bus_services_data, "bus_services")

        return bus_services_data

    def handle_arrivals(self, data):
        bus_timings = data.get("Services")

        if bus_timings:
            all_services = []

            bus_stops_data = self.read_file("bus_stops_2024_02_02")
            bus_stop_info = next(
                (
                    stop
                    for stop in bus_stops_data
                    if stop["BusStopCode"] == str(data.get("BusStopCode"))
                ),
                None,
            )
            for bus_service in bus_timings:
                single_service = {
                    "serviceNo": bus_service.get("ServiceNo"),
                    "operator": bus_service.get("Operator"),
                    "busStopInfo": bus_stop_info,
                    "timings": [],
                }

                for next_bus_key in ["NextBus", "NextBus2", "NextBus3"]:
                    next_bus = bus_service.get(next_bus_key, None)
                    next_bus_arrival = next_bus.get("EstimatedArrival", None)
                    if next_bus_arrival:
                        single_arrival = {
                            "minutes": calculate_time(next_bus_arrival),
                            "load": next_bus.get("Load"),
                            "feature": next_bus.get("Feature"),
                            "type": next_bus.get("Type"),
                        }
                        single_service["timings"].append(single_arrival)

                all_services.append(single_service)
            return all_services
        return None
