import requests
import datetime
import json


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.BASE_URL = "http://datamall2.mytransport.sg/ltaodataservice/"
        self.HEADERS = {"Accept": "application/json", "AccountKey": self.api_key}

    def _make_request(self, endpoint, params=None):
        response = requests.get(
            self.BASE_URL + endpoint, headers=self.HEADERS, params=params
        )

        return response.json() if response.status_code == 200 else None

    def _make_loop_requests(self, endpoint, offset=0):
        offset = 0
        limit = 500
        all_data = []

        while True:
            offset_url = f"{endpoint}?$skip={offset}"
            request_data = self._make_request(offset_url).get("value")
            if request_data:
                all_data.extend(request_data)
                offset += limit
            else:
                break

        return all_data

    def save_to_file(self, data, filename):
        current_date = datetime.datetime.now().date()
        current_date_str = current_date.strftime("%Y_%m_%d")
        filename = f"./data/{filename}_{current_date_str}.json"
        json_data = {"last_modified": current_date_str, "records": data}
        with open(filename, "w") as file:
            json.dump(json_data, file)

    def read_file(self, directory):
        f = open(f"data/{directory}.json")
        file_data = json.load(f)["records"]
        return file_data
