import random

name_string = input("Give me everybody's names, seperated by a comma.\n")
names = name_string.split(",")
new_names = [item.replace(' ', '') for item in names]
# random_integer = random.randrange(len(new_names))
# print(f"{new_names[random_integer]} is going to pay the bill.")
print(f"{random.choice(new_names)} is going to pay the bill.")
