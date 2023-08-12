import requests
from datetime import datetime
from config import AUTH_PARAMS, EXCERCISE_POST_URL, SHEETY_POST_URL, SHEETY_AUTH_PARAMS, EXERCISE_PARAMETERS, SHEETY_PARAMETERS

def get_todays_date_and_day():
    '''This function takes todays date and day and return it in the form of a string in YYYYMMDD and day of the week format'''
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    day = now.strftime("%A")
    return date, day

query = input("What did you do today?")
EXERCISE_PARAMETERS["query"] = query

# Get data from Nutritionix API
res = requests.post(EXCERCISE_POST_URL, json=EXERCISE_PARAMETERS, headers=AUTH_PARAMS)
res.raise_for_status()
data = res.json()

# # Write data to the google sheet
def write_to_google_sheet():
    res = requests.post(SHEETY_POST_URL, json=SHEETY_PARAMETERS, headers=SHEETY_AUTH_PARAMS)
    res.raise_for_status()
    print(res.text)

def get_sheety_parameters(data):
    '''This function populates the sheety parameters and then call the post to google sheets method'''
    date, day = get_todays_date_and_day()
    data = data["exercises"]
    for exercise in data:
        SHEETY_PARAMETERS["sheet1"]["date"] = date
        SHEETY_PARAMETERS["sheet1"]["day"] = day
        SHEETY_PARAMETERS["sheet1"]["exercise"] = exercise["name"]
        SHEETY_PARAMETERS["sheet1"]["duration"] = str(exercise["duration_min"])
        SHEETY_PARAMETERS["sheet1"]["calories"] = exercise["nf_calories"]

        # Call the sheety post function here
        print(SHEETY_PARAMETERS)
        write_to_google_sheet()

    

get_sheety_parameters(data)





