from turtle import Turtle
import random

# Defined class (Superclass)
# Now the food class will inherit from the Turtle calss


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # The original pixel will be 20X20px
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)
