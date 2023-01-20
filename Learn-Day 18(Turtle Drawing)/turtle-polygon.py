# Importing the modules ways:
# import turtle
# from turtle import * ##Everything
# import turtle as t

from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.color("gray70")

colors = ["steel blue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "CornflowerBlue", "powder blue"]

for num_sides in range(3, 11):
    angle = 360 / num_sides
    tim.color(random.choice(colors))
    for _ in range(num_sides+1):
        tim.forward(100)
        tim.right(angle)


# def Movement():
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# for i in range(15):
#     Movement()


screen = Screen()
screen.exitonclick()
