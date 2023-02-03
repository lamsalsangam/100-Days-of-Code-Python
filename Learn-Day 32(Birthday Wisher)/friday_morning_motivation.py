import smtplib
import datetime as dt
import random

MY_EMAIL = "Put your gmail here"
MY_PASSWORD = "Put your password here"
YOUR_EMAIL = "Put the destination email here"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:  # Friday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # connection = smtplib.SMTP('smtp.gmail.com')
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=YOUR_EMAIL,
                            msg=f"Subject:Friday Motivation\n\n{quote}")
