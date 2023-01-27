# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# There is the inbuilt library that will help with the csv
'''

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)  # It will create the csv reader object
    #  So it can be looped through
    # for row in data:
    #     print(row)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
'''

# There is too much faff involved in the process above

# Therefore the pandas is used to make the task easier

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
####################
# average = sum(temp_list)/len(temp_list)
# print(average)
# print(data["temp"].mean())
####################
# print(data["temp"].max())

# Get the data in the columns
# print(data["condition"])
# print(data.condition)

# Get the data in the row
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])


################
# print(data[data.temp == data.temp.max()])
# print(data[data["temp"] == data["temp"].max()])


# monday = data[data.day == "Monday"]
# # print(monday.condition)

# print((monday.temp * 9/5)+32)

#################
# Create the data frame from the scratch


# data_dict = {
#     "students": ["Ram", "Hari", "Krishna"],
#     "scores": [1, 10, 16000]
# }

# data_0 = pandas.DataFrame(data_dict)
# data_0.to_csv("new_data.csv")
# print(data_0)
