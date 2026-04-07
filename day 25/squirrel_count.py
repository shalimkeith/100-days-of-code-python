import pandas as pd

data = pd.read_csv("Central_Park_Squirrel_Census_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] =="Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] =="Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] =="Cinnamon"])


print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Red","Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")

# data = pd.DataFrame(primary_color_count)
# data.to_csv("color_count_data.csv")