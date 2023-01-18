# https://pypi.org/ packages form here
# Pretty Table packages https://pypi.org/project/prettytable/

from prettytable import PrettyTable
import os

table = PrettyTable()  # Declaration of the instab=nces of the class
"""
# Row wise table

table.field_names = ["Family Name", "First Name",
                     "HomeTown"]  # Here "field_name" is the attribute
table.add_row(["Lamsal", "Sangam", "Syangja"])
table.add_row(["Lamsal", "Saurav", "Syangja"])
table.add_row(["Lamsal", "Sanjog", "Syangja"])
table.add_row(["Dhungana(Lamsal)", "Bhuwaneshori", "Syangja"])
table.add_row(["Lamsal", "Jagannath", "Syangja"])
"""
# Column wise table
table.add_column(
    "First Name", ["Jagannath", "Bhuwaneshori", "Sangam", "Saurav", "Sanjog",])
table.add_column(
    "Family Name", ["Lamsal", "Lamsal", "Lamsal", "Lamsal", "Lamsal"])
table.add_column("HomeTown", ["Syangja", "Syangja",
                 "Syangja", "Syangja", "Syangja"])
os.system("cls")
table.align = "r"
table.align["First Name"] = "l"
print(table)
