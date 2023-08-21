import requests
import datetime as dt
from config import TOKEN, USERNAME

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

def get_todays_date():
    '''This function takes todays date and return it in the form of a string in YYYYMMDD format'''
    today = dt.date.today()
    today = today.strftime("%Y%m%d")
    return today

# HTTP Headers
headers = {
    "X-USER-TOKEN": TOKEN,
}

# Params for creating a new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Params for creating a new Graph
graph_params = {
    "id": "graph1",
    "name": "inoffice-graph",
    "unit": "days",
    "type": "int",
    "color": "shibafu",
}

graph_update_params = {
    "name": "inoffice-graph",
    "unit": "days",
    "type": "int",
    "color": "shibafu",
}

PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{graph_params['id']}"

# Params for updating the pixel on the graph
pixel_params = {
    "date": get_todays_date(),
    "quantity": "1",
}

# print(pixel_params)

# User has been created so commenting line 14 and 15 out.
# res = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(res.text)
# {"message":"Success. Let's visit https://pixe.la/@jeronimo , it is your profile page!","isSuccess":true}

# Setup inoffice attendance tracking graph
# grapph address https://pixe.la/v1/users/jeronimo/graphs/graph1.html
# commenting out lines 34 and 35 as the graph is created
# res = requests.post(PIXELA_GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(res.text)

# Update the graph parameters
# Done : Updated the graph params to days
# res = requests.put(PIXEL_ENDPOINT, json=graph_update_params, headers=headers)
# print(res.text)

# Sending a pixel to the graph
# Went to office on this day
res = requests.post(PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(res.text)


# Deleting the pixel
# res = requests.delete(f"{PIXEL_ENDPOINT}/{get_todays_date()}", json=pixel_params, headers=headers)
# print(res.text)
        

