import requests
import datetime

TOKEN = "fb1e7ed1a080"
USERNAME = "shadow"
GRAPH_ID = "graphHQL1"

pixela_endpoint = "https://pixe.la/v1/users"

# Creating the new user account on pixe.la

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# After creating the user with the code below please be sure to comment it out
requests.post(url=pixela_endpoint, json=user_params)  # -----> #


# Creating the Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Commitment",
    "unit": "Hours",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# After creating the graph with the code below please be sure to comment it out
requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Posting the value in the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime(year=2022, month=7, day=23)

pixel_data = {
    "data": today.strftime("%Y%m%d"),
    "quantity": "1",
}

requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)


# HTTP Put and Delete request. Update the task in endpoint
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# to update the endpoint
requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# Delete the task from the endpoint
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

requests.delete(url=delete_endpoint, headers=headers)
