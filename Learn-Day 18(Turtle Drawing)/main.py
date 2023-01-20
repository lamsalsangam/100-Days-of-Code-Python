import turtle as t
import random
# import colorgram

friend = t.Turtle()
t.colormode(255)

# rgb_colors_palettes = []
color_palettes = [(2, 2, 1), (97, 191, 221), (239, 230, 224), (211, 135, 157), (182, 157, 135), (192, 216, 233), (131, 211, 234), (237, 162, 186), (36, 15, 23), (46, 107, 151), (115, 97, 61), (30, 171, 207), (12, 42, 16), (140, 71, 90),
                  (194, 90, 113), (15, 27, 50), (130, 166, 39), (152, 18, 46), (220, 232, 226), (10, 56, 141), (137, 179, 153), (212, 201, 135), (68, 110, 74), (209, 88, 69), (175, 185, 222), (226, 174, 167), (69, 90, 19), (34, 85, 39), (104, 117, 172)]
# colors = colorgram.extract('hirst.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_palette = (r, g, b)
#     rgb_colors_palettes.append(color_palette)

# print(rgb_colors_palettes)

friend.ht()
friend.penup()
friend.setheading(225)
friend.forward(300)
friend.setheading(0)


def positional():
    friend.setheading(90)
    friend.forward(50)
    friend.setheading(180)
    friend.forward(500)
    friend.setheading(0)


def create_dot():
    for i in range(10):
        friend.dot(20, random.choice(color_palettes))
        # friend.penup()
        friend.forward(50)


for i in range(10):
    create_dot()
    positional()


screen = t.Screen()
screen.exitonclick()
