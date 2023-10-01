"""
 This script gets the current price of the requested product from Amazon, 
 compares the price to target price and then sends an email if the price 
 is less than target price.
"""

import smtplib

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import GMAIL_USER, GMAIL_PASSWORD, RECEIVER_EMAIL, TRACKER_URL, TARGET_PRICE


# Keep browser running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(TRACKER_URL)

price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

price = float(price_dollars.text) + float(price_cents.text)

driver.quit()


def send_email():
    """This function sends an email if the Amazon item is below the Target Price"""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USER, password=GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_USER,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject: Amazon Price Alert\n\nHey! Good news!!!\nThe currently tracked Amazon Product \n\n{TRACKER_URL}\n\n is below your set target price. Head over and purchase now :)",
        )
        connection.close()
    print("sent email")


if price <= TARGET_PRICE:
    send_email()
