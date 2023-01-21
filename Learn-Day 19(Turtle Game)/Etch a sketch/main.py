import turtle as t

friend = t.Turtle()
screen = t.Screen()


friend.speed(10)


def move_forward():
    friend.forward(10)


def move_backward():
    friend.backward(10)


def left():
    current_heading = friend.heading()
    friend.setheading(current_heading + 10)


def right():
    current_heading = friend.heading()
    friend.setheading(current_heading - 10)


def clear_screen():
    friend.reset()


screen.listen()
# When we pass the function as an arguments we don't put parenthesis at the end
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
