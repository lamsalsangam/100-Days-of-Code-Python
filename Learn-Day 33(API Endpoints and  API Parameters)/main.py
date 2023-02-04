import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 27.674300
MY_LONG = 85.374896
MY_EMAIL = "Put your email here"
MY_PASSWORD = "Put your password here"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    # To get the desired data
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= latitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:Look up.👆👆\n\nThe ISS is abovve you in the sky")
