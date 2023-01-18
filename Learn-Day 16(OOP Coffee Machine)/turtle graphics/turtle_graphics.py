# In every download of the python the turtle graphics comes with it
# It is the class predefned for the somewhat copy of tortorise
from turtle import Turtle, Screen

# Defining the object(Instances) form the class "Turtle" which is in fact the blueprint
# By assigning the class to the variable we indeed defined the object
sangam = Turtle()

# Changing the shap to look like an actual turtle
sangam.shape("turtle")  # Method(Function)
# Changing the color of the turtle
# sangam.color("chartreuse4")
sangam.color("azure4")

# To move forward by [...] paces
# We can also use fd(..)
sangam.forward(100)

# The Screen represent the object in which the above turtle is going to show up
my_screen = Screen()

# Object Attributes (Variables)
# print(my_screen.canvheight)
# Height of the canvas in which the turtle is shown
# my_screen.canvheight #--> is an attribute of the object(Instances)
# Object Method (Function)
# Instead of quickly showing up and quickly dissappearing when our code end
# "exitonclick" method will allow the program to continue running until we click on screen.
my_screen.exitonclick()  # Method
