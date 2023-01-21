import turtle as t
import random


screen = t.Screen()
# setup will allow us to set up the size and  position of the main window.
screen.setup(width=500, height=400)  # (Width, Height) ## Method
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter the choice: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# friend = t.Turtle(shape="turtle")
# Its a coordinates of the graph we just need to half the setup data to get the starting line
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-239, y=y_position[turtle_index])  # (x,y)
    # friend.goto(x=-239, y=-100+(turtle_index*40))  # (x,y)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(
                        f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(
                        f"You've lost! The {winning_color} turtle is the winner!")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
