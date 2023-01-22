import turtle as t
# import time

# segment_1 = t.Turtle('square')


# def total_snake():
#     segment_1.color('white')


screen = t.Screen()
screen.title("Snake Game")
screen.bgcolor('black')
screen.setup(width=600, height=600)
# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-10, 0)]

segments = []

for position in starting_position:
    new_segment = t.Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# segment_1 = t.Turtle('square')
# segment_1.color('white')
# segment_2 = t.Turtle('square')
# segment_2.color('white')
# segment_2.goto(x=-20, y=0)
# segment_3 = t.Turtle('square')
# segment_3.color('white')
# segment_3.goto(x=-40, y=0)


# total_snake()


game_is_on = True
while game_is_on:
    # Perform a TurtleScreen update.
    screen.update()
    # time.sleep(1)
    # for seg_num in range(start=2, stop=0, step=-1):
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
