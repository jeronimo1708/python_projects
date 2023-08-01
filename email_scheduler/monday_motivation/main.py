
import random
import smtplib
import datetime as dt
import sys
sys.path.append("/home/jeronimo/dev/python_projects/email_scheduler/")
from config import GMAIL_PASSWORD, GMAIL_USER

curr_date = dt.datetime.now()
year = curr_date.year
month = curr_date.month
day = curr_date.day
# Weekday function returns the day of the week 0 => Monday and 6=> Sunday
day_of_week = curr_date.weekday()

def generate_quote():
    '''This function generates a random quote from the quotes.txt file'''
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        message_text = random.choice(quotes)
    return message_text

if day_of_week == 0:
    message_text = generate_quote()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_USER, to_addrs="dcosta.j17@outlook.com", msg=f"Subject: Monday Motivation\n\n{message_text}" )
        connection.close()
        print("sent message")

