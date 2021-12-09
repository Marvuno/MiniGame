from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.high_score = 0
        self.score = -1
        with open("snake/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.speed(0)
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}", align="center", font=("Courier", "24", "bold"))

    def game_over(self):
        self.high_score = max(self.high_score, self.score)
        self.score = -1
        with open("snake/data.txt", 'w') as data:
            data.write(str(self.high_score))
        self.update()
