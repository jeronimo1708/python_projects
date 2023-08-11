import os
import requests
import datetime as dt
from config import NEWS_API_KEY, ALPHA_VANTAGE_API_KEY

# Twilio imports
from twilio.rest import Client
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, TWILIO_TO_NUMBER


def send_sms(message_body):
    """This function sends a message to the specified number in the config file"""
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        to=TWILIO_TO_NUMBER, from_=TWILIO_FROM_NUMBER, body=message_body
    )

    print(message.status)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# JSON KEYS FOR STOCK PRICES
TIME_SERIES_DATA = "Time Series (Daily)"
DATE_TODAY = dt.date.today()
DATE_TODAY_STR = DATE_TODAY.strftime("%Y-%m-%d")
DATE_YESTERDAY = dt.date.today() - dt.timedelta(days=1)
DATE_YESTERDAY_STR = DATE_YESTERDAY.strftime("%Y-%m-%d")
DATE_BEFORE_YESTERDAY = dt.date.today() - dt.timedelta(days=2)
DATE_BEFORE_YESTERDAY_STR = DATE_BEFORE_YESTERDAY.strftime("%Y-%m-%d")

OPEN = "1. open"
HIGH = "2. high"
LOW = "3. low"
CLOSE = "4. close"
VOLUME = "5. volume"

# JSON KEYS FOR NEWS API
ARTICLES = "articles"
TITLE = "title"
DESCRIPTION = "description"
URL = "url"
CONTENT = "content"

# Get stock data
stock_prices_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_VANTAGE_API_KEY}"
response = requests.get(stock_prices_url)
data = response.json()

# Get yesterday's and Day before yesterday's price 
price_yesterday = float(data[TIME_SERIES_DATA][DATE_YESTERDAY_STR][CLOSE])
price_day_before_yesterday = float(
    data[TIME_SERIES_DATA][DATE_BEFORE_YESTERDAY_STR][CLOSE]
)
# Check if price diff is more than 5%
five_percent = price_yesterday / 200
diff_prices = abs(price_yesterday - price_day_before_yesterday)

# If diff > 5%, then search for news articles related to that stock and send a brief of 3 articles to the user.
if diff_prices > five_percent:
    print("Get news")
    news_url = f"https://newsapi.org/v2/everything?q={STOCK}&apiKey={NEWS_API_KEY}"
    response = requests.get(news_url)
    data = response.json()
    data = data[ARTICLES][:3]
    #TODO: Twilio is extremely slow, so i need to try sending sms at a later time.
    for article in data:
        title = article[TITLE]
        description = article[DESCRIPTION]
        message_body = f"{STOCK} \n Headline: {title}\n\n Brief: {description}"
        send_sms(message_body)

