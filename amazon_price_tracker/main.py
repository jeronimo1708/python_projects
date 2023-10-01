import smtplib
import requests
from bs4 import BeautifulSoup

from config import GMAIL_USER, GMAIL_PASSWORD, RECEIVER_EMAIL, HEADERS, TRACKER_URL, TARGET_PRICE


res = requests.get(TRACKER_URL, headers=HEADERS)
res.raise_for_status()
data = res.text
soup = BeautifulSoup(data, "html.parser")
data = soup.select_one(".a-price-whole")
data = data.text
data = data.replace(".", "")
current_price = int(data)


def send_email():
    '''This function sends an email if the Amazon item is below the Target Price'''
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_USER, to_addrs=RECEIVER_EMAIL, msg=f"Subject: Amazon Price Alert\n\nHey! Good news!!!\nThe currently tracked Amazon Product \n\n{TRACKER_URL}\n\n is below your set target price. Head over and purchase now :)" )
        connection.close()
    print("sent email")
    

if current_price <= TARGET_PRICE:
    send_email()
    

