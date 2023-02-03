import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "Put your email here."
MY_PASSWORD = "Put your password here."

today = (dt.datetime.now().month, dt.datetime.now().day)
print(today)

data = pandas.read_csv("birthdays.csv")
# print(data.day)
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
birthdays_dict = {(data_row.month, data_row.day): data_row for (
    index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=birthdays_person["email"], msg=f"Subject:Happy Birthday\n\n{contents}")


# Host it on pythonanywhere to run it everyday without any effort
