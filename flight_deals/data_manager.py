import requests
from config import SHEETLY_TOKEN, SHEETLY_AUTH_PARAMS, SHEETLY_URL, SHEETLY_NAME, SHEETLY_PUT_URL

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._post_url = SHEETLY_URL
        self._get_url = SHEETLY_URL
        self._put_url = SHEETLY_PUT_URL
        self._sheetly_auth_params = SHEETLY_AUTH_PARAMS
        self._sheetly_token = SHEETLY_TOKEN
        self.sheetly_name = SHEETLY_NAME
        self.test_post_json = {SHEETLY_NAME:{"city": "New York City", "iataCode": "JFK", "lowestPrice": 300}}

    def post_data(self, data={}):
        response = requests.post(self._post_url, json=data, headers=self._sheetly_auth_params)
        # response.raise_for_status()
        print(response.text)

    def get_data(self):
        response = requests.get(self._post_url, headers=self._sheetly_auth_params)
        response.raise_for_status()
        data = response.json()
        return data["prices"]
    
    def put_data(self, data={}, object_id=None):
        response = requests.put(self._put_url.format(object_id=object_id), json=data, headers=self._sheetly_auth_params)
        response.raise_for_status()

