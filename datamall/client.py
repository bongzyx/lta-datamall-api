import requests


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.BASE_URL = "http://datamall2.mytransport.sg/ltaodataservice/"
        self.HEADERS = {"Accept": "application/json", "AccountKey": self.api_key}

    def _make_request(self, endpoint, params=None):
        response = requests.get(
            self.BASE_URL + endpoint, headers=self.HEADERS, params=params
        )

        return response.json()
