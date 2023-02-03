# import smtplib

# my_email = "Put your email here"
# password = "Put your password here"

# # If specified, host is the name of the remote host to which to connect
# # connection = smtplib.SMTP("smtp.gmail.com")
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Start the Transport layer Security
#     # It is the way of securing our connection to the email server
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="winoda9090@chotunai.com", msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
