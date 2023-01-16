import random
import os
from game_data import data
import art


def choice():
    os.system("cls")
    info_A = random.choice(data)
    info_B = {}
    score = 0
    game_finished = False
    print(art.logo)
    while not game_finished:
        choice_finished = False
        while not choice_finished:
            info_B = random.choice(data)
            if info_B != info_A:
                choice_finished = True
        greater = compare(info_A, info_B)
        display(info_A, info_B)
        choosen = input("Who has more followers, Type 'A' or 'B': ")
        if greater == choosen:
            os.system("cls")
            print(art.logo)
            score += 1
            print(f"You're right! Current score: {score}.")
            info_A = info_B if greater == "A" else info_A
        else:
            os.system("cls")
            print(art.logo)
            print(f"Sorry, that's wrong, Final score {score}")
            game_finished = True


def compare(info_1, info_2):
    if info_1["follower_count"] > info_2["follower_count"]:
        return "A"
    else:
        return "B"


def display(info_a, info_b):
    print(
        f"Compare A: {info_a['name']}, a {info_a['description']}, from {info_a['country']}")
    print(art.vs)
    print(
        f"Against B: {info_b['name']}, a {info_b['description']}, from {info_b['country']}")


choice()
