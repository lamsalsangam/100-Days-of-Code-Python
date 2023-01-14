# Local Scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()

# Global Scope

# player_health = 10


# def drink_potion():
#     potion_strength = 2
#     print(player_health)


# drink_potion()
# print(player_health)

# Therer is no Block scope in Python

# game_level = 3
# enemies = ["Skeleton", "Zombie", "ALien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)


# Modifing Global Scope

# enemies = 1


# def increase_enemies():
#     # Don't change the global scope like this because it can impose bug in the program
#     # global enemies
#     print(f"enemies inside the  function: {enemies}")
#     # Do this for the better program experience
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside the function: {enemies}")


# Global Constants

# PI = 3.141549
