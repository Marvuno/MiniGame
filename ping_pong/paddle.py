from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(x=positions[0], y=positions[1])
        self.color("white")

    def up(self):
        y_cor = self.ycor() + 20
        self.goto(x=self.xcor(), y=y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=y_cor)