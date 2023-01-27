import pandas

data = pandas.read_csv("squirrel_count.csv")

cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Color": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
