from turtle import Turtle
from turtle_crossing_game.pause import Pause


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.ht()
        self.penup()
        self.goto(x=-280, y=240)
        self.update()

    def level_up(self):
        self.level += 1
        Pause().countdown()
        self.clear()
        self.update()

    def update(self):
        self.write(arg=f"Level: {self.level}", align="left", font=("Courier", 28, "bold"))

    def lost(self):
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over", align="center", font=("Courier", 36, "bold"))


class Cheat(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("red3")
        self.penup()
        self.goto(x=0, y=-260)
        self.write(arg="Cheater! You Suck!", align="center", font=("Courier", 36, "bold"))
