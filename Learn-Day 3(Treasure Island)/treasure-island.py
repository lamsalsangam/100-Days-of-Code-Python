print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input(
    'You\'re at cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input(
        'You\'re at the lake. You need to reach the island in the middle of the lake. What do you want to do? Type "swim" or "wait"\n').lower()
    if choice2 == "wait":
        choice3 = input(
            'You\'re at the final hurdle. There is the house with 3 doors. Which door would you pick? Type "Red" or "Blue" or "Yellow"\n').lower()
        if choice3 == "yellow":
            print("\n\n!!!Congratualations!!! You won the greatest treasure chest!")
        elif choice3 == "red":
            print("You've entered the domain of fire. Game Over!!")
        elif choice3 == "blue":
            print("You've entered the domain of ice. Game Over!!")
        else:
            print("You've choosen the door that doesn't exists. Game Over!!")
    else:
        print("Shark ate you. Game Over!!")
else:
    print("You got ambused by the bandit. Game Over!!")
