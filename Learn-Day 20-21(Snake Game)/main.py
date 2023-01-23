from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Screen is going to update in every 0.1 seconds
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food
    # Distance form the first segment of the snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect the coliision with the tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         # if head collides with the any segments in the tail
    #         game_is_on = False
    #         score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # if head collides with the any segments in the tail
            game_is_on = False
            score.game_over()

screen.exitonclick()
