from turtle import Turtle


AILGNMENT = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",
                   align=AILGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over",
                   align=AILGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
