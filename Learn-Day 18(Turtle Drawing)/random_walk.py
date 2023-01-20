# from turtle import Turtle, Screen
import turtle as t
import random

# colors = ["steel blue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
#           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "CornflowerBlue", "powder blue"]
positions = [0, 90, 180, 270]

# tuples are some thing of sort like that are carved into the stone which means that it cannot be changed


friend = t.Turtle()
t.colormode(255)


def random_colors():
    r = random.randint(0, 255-1)
    g = random.randint(0, 255-1)
    b = random.randint(0, 255-1)
    random_color = (r, g, b)
    return random_color


friend.pensize(10)
friend.speed(0)
for _ in range(300):
    # friend.color(random.choice(colors))
    friend.color(random_colors())
    friend.forward(30)
    friend.seth(random.choice(positions))


screen = t.Screen()
screen.exitonclick()
