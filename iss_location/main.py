import requests
import smtplib
import datetime as dt
from time import sleep
from config import GMAIL_USER, GMAIL_PASSWORD, RECEIVER_EMAIL

MY_LAT = 40.728157
MY_LON = -74.077644
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"
ISS_POSITION_API = "http://api.open-notify.org/iss-now.json"
parameters = {
    "lat":MY_LAT,
    "lon":MY_LON,
    "formatted":0,
}

def check_if_dark_outside():
    '''This function checks if the current time is after sunset and before sunrise'''
    global parameters
    current_time = dt.datetime.now()
    current_hour = current_time.hour
    response = requests.get(url=SUNRISE_SUNSET_API, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if current_hour > sunset or current_hour < sunrise:
        return True
    return False
    
def check_where_ISS_is():
    '''Returns the current position of the ISS space station'''
    response = requests.get(url=ISS_POSITION_API)
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])
    return iss_lat, iss_lon

def send_email():
    '''This function sends an email if the ISS space station is near your city'''
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_USER, to_addrs=RECEIVER_EMAIL, msg=f"Subject: ISS Space Station\n\nLook up!!!\nThe ISS Space Station is near you" )
        connection.close()

def is_ISS_overhead():
    '''This function check if the ISS is near you and initiates the send email function'''
    iss_lat, iss_lon = check_where_ISS_is()
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LON-5 <= iss_lon <= MY_LON+5:
        print("ISS is here")
        send_email()
    else:
        print("ISS is not near you")

## The main loop. It will keep running from sunset to sunrise
while check_if_dark_outside():
    is_ISS_overhead()
    sleep(60)

    










