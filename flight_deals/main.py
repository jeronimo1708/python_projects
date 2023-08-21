from data_manager import DataManager
from flight_search import FlightSearch

sheetly_data_object = DataManager()
# google_sheet_data = sheetly_data_object.get_data()

# this populates the IATA code for the city and lowest price in the Google Sheet
flight_search = FlightSearch()
# for data_row in google_sheet_data:
#     if not data_row.get("iataCode"):        
#         iata_code = flight_search.get_iata_code(data_row["city"])
#         data = {
#             sheetly_data_object.sheetly_name:{
#                 "iataCode": iata_code,
#                 "id": data_row["id"],
#             }
#         }
#         sheetly_data_object.put_data(object_id=data_row["id"], data=data)


flight_data = flight_search.search_flights("PAR")
print(flight_data.price)