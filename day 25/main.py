# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas
import statistics
data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(statistics.mean(temp_list))
#
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# print(data["temp"].max())
#
# print(data["condition"])
#
# data.condition
#
# print(data.day)
#
# print(data.temp)
# print(data[data["temp"] == data["temp"].max()])
# print(data[data.day == data.day.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 +32
#
# print(monday_temp_f)

#monday = data[data.day == "Monday"]
# monday_temp = int(monday["temp"].iloc[0])
# monday_temp_f = monday_temp * 9/5 + 32
#
# print(monday_temp_f)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday["temp"].iloc[0])
# monday_temp_f = monday_temp * 9/5 + 32
#
# print(monday_temp_f)


data_dict = {
    "students": ["Shalim Keith", "Bucky", "Charles"],
    "scores": [94,34,99]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")