from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.goto(x=0, y=240)
        self.l_score = 0
        self.r_score = 0
        self.update()

    def right_win(self):
        self.r_score += 1
        self.clear()
        self.update()

    def left_win(self):
        self.l_score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(arg=f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 36, "bold"))
