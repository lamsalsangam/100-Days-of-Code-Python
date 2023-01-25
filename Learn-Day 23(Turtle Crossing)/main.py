import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing.")
screen.tracer(0)


tortorise = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tortorise.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect the collision with the car
    for car in car_manager.all_cars:
        if car.distance(tortorise) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the turtle reach the other side of the screen
    if tortorise.is_at_finish_line():
        tortorise.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
