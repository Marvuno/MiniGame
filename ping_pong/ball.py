from turtle import Turtle
from ping_pong.pause import Pause


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("violet")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.play = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        # Reset ball speed
        for _ in range(self.play):
            self.x_move /= 1.1
            self.y_move /= 1.1
        self.play = 0
        # 2 Second until next round
        pause = Pause()
        pause.countdown()
