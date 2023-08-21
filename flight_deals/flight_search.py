import requests
import datetime as dt
from flight_data import FlightData
from config import KIWI_API, KIWI_AUTH_PARAMS, FROM_DEST, KIWI_SEARCH_URL, KIWI_SEARCH_AUTH_PARAMS


class FlightSearch:
    def __init__(self):
        # todays date
        today = dt.datetime.today()
        # tomorrows date
        tomorrow = today + dt.timedelta(days=1)
        # date from parameter in string
        self.date_from = tomorrow.strftime("%d/%m/%Y")
        # six months ahead date from tomorrows date
        six_months_ahead = tomorrow + dt.timedelta(days=180)
        # date to parameter in string
        self.date_to = six_months_ahead.strftime("%d/%m/%Y")
        # return range
        return_start_range = tomorrow + dt.timedelta(days=7)
        return_end_range = return_start_range + dt.timedelta(days=28)
        # return range in string
        self.return_from = return_start_range.strftime("%d/%m/%Y")        
        self.return_to = return_end_range.strftime("%d/%m/%Y")

    def get_iata_code(self, city):
        parameters = {
            "term": city,
            "location_types": "city",
        }
        res = requests.get(KIWI_API, params=parameters, headers=KIWI_AUTH_PARAMS)
        res.raise_for_status()
        data = res.json()
        data = data["locations"][0]["code"]
        return data
    
    def search_flights(self, to_city):
        ''' This function get the flight data for each destination city '''
        parameters = {
            "fly_from": FROM_DEST,
            "fly_to": to_city,
            "date_from" : self.date_from,
            "date_to" : self.date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        res = requests.get(KIWI_SEARCH_URL, params=parameters, headers=KIWI_SEARCH_AUTH_PARAMS)
        res.status_code
        data = res.json()
        # The response object return a list with one dictionary inside it
        # Hence sending the first item in the list (which is a dict) to clean the data
        data = data.get("data")
        data = data[0]
        price = data.get("price")
        origin_city = data.get("cityFrom")
        origin_airport = data.get("flyFrom")
        destination_city = data.get("cityTo")
        destination_airport = data.get("flyTo")
        out_date = data.get("local_departure")
        out_date = out_date.split("T")[0]
        return_date = data.get("local_arrival")
        return_date = return_date.split("T")[0]
        flight_data = FlightData(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date)
        return flight_data
        # self.clean_data(data)

    def clean_data(self, data):
        '''This function cleans the data and passed it on to the Flight data creator method'''
        data = data.get("data")
        data = data[0]
        price = data.get("price")
        origin_city = data.get("cityFrom")
        origin_airport = data.get("flyFrom")
        destination_city = data.get("cityTo")
        destination_airport = data.get("flyTo")
        out_date = data.get("local_departure")
        out_date = out_date.split("T")[0]
        return_date = data.get("local_arrival")
        return_date = return_date.split("T")[0]
        flight_data = FlightData(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date)
        return flight_data
        # self.create_flight_data(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date)

    def create_flight_data(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        '''This function creates a Flight Data object'''
        flight_data = FlightData(price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date)
        return flight_data

        
