import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()
# question_data["results"] return a list of questions along with other info in the form of a dictionary from the API
question_data = question_data["results"]
