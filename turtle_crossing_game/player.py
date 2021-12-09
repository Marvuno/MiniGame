from turtle import Turtle
from turtle_crossing_game.scoreboard import Cheat


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("SlateBlue")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)
        self.shape("turtle")

    def move(self):
        self.forward(20)

    def advance(self):
        self.ht()
        self.goto(x=0, y=-280)
        self.st()

    def cheater(self):
        self.goto(x=0, y=280)
        Cheat()

