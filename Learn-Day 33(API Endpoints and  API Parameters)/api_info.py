# http://api.open-notify.org/iss-now.json
# How to access the API Endpoint in python
import requests

# Response and its meaning
# 1XX : Hold On
# 2XX: Here you Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

# Firstly make the request
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # # if response.status_code != 200:
# # # raise Exception("Bad response from the ISS API")
# if response.status_code == 404:
#     raise Exception("The resources doesn't exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data")

# To raise the exception for the bad response circumtances
response.raise_for_status()

# To get the desired data
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
