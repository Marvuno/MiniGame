from turtle import Turtle
import time


class Pause(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("black")
        self.penup()

    def countdown(self):
        self.write(arg="2", align="center", font=("Courier", 36, "bold"))
        time.sleep(1)
        self.clear()
        self.write(arg="1", align="center", font=("Courier", 36, "bold"))
        time.sleep(1)
        self.clear()
