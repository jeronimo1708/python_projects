import os
import csv
import random
import smtplib
import datetime as dt
import sys
sys.path.append("/home/jeronimo/dev/python_projects/email_scheduler/")
from config import GMAIL_USER, GMAIL_PASSWORD

TEMPLATE_DIR = "letter_templates"
TEMPLATES_FILES = os.listdir(TEMPLATE_DIR)
STRING_TO_REPLACE = "[NAME]"


def get_today():
    '''This function returns todays date, month, year'''
    curr_date = dt.datetime.now()
    year = curr_date.year
    month = curr_date.month
    day = curr_date.day
    return year, month, day

def generate_birthday_message(name):
    '''This function reads the template file, adds the name of the person whose birthday it is and returns the greeting as a string'''
    unique_greeting_file = f"{TEMPLATE_DIR}/{random.choice(TEMPLATES_FILES)}"        
    with open(unique_greeting_file, "r") as file:
        birthday_greetings = file.readlines()
    birthday_greetings[0] = birthday_greetings[0].replace(STRING_TO_REPLACE, name)
    return "".join(birthday_greetings)

def send_birthday_message(message_text, email):
    '''This function sends the birthday greeting to the person whose birthday it is as per the birthdays.csv file'''
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_USER, to_addrs=email, msg=f"Subject: Happy Birthday\n\n{message_text}" )
        connection.close()
        print("sent message")


today_year, today_month, today_day = get_today()

with open("birthdays.csv") as file:
    birthday_info = file.readlines()
    for birthday in birthday_info:
        bday = birthday.split(',')
        name, email, year, month, day = bday[0], bday[1], int(bday[2]), int(bday[3]), int(bday[4][:2])

        if month == today_month and day == today_day:
            message_text = generate_birthday_message(name)
            send_birthday_message(message_text, email)

        
    


# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




