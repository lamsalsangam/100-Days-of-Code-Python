programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

# Create an empty dictionary
empty_dictionary = {}

# To Empty out the existing dictionary
programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# To Loop through the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lillie", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a List in a List

["A", "B", ["C", "D"], "E"]

# Nesting Dictionary in a Dictionary
# Accessed by the key associated

travel_log = {
    "France": {"cities_visited": ["Paris", "Lillie", "Dijon"],
               "total_visits": 12,
               },
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
                "total_visits": 5,
                }
}

# Nesting Dictionary in side the Lists
# Accessed by the index

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lillie", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    }
]
