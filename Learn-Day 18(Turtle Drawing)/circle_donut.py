import turtle as t
import random

heading_list = []


friend = t.Turtle()
friend.speed(0)  # Fastest 0-->10 # 0 being the fastest
t.colormode(255)


def random_colors():
    r = random.randint(0, 255-1)
    g = random.randint(0, 255-1)
    b = random.randint(0, 255-1)
    random_color = (r, g, b)
    return random_color


# for i in range(0, 361, 5):
#     heading_list.append(i)

# for position in heading_list:
#     friend.circle(100)
#     friend.setheading(current_heading + position)
#     friend.color(random_colors())

def draw_spirograh(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        friend.circle(100)
        current_heading = friend.heading()
        friend.setheading(current_heading + size_of_gap)
        friend.color(random_colors())


draw_spirograh(5)
screen = t.Screen()
screen.exitonclick()
