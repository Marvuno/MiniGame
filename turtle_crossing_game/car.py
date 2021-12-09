from turtle import Turtle
import random

COLOR = ["red", "yellow", "orange", "blue", "green", "purple",
         "aquamarine", "chocolate1", "DarkViolet", "Coral", "magenta", "SeaGreen2"]


class Car:

    def __init__(self):
        self.cars = []
        self.speed = 10
        for _ in range(10):
            self.create()
            self.initial()

    def initial(self):
        for car in self.cars:
            car.goto(x=random.randrange(-80, 320, 40), y=random.randrange(-240, 280, 40))

    def create(self):
        new = Turtle("square")
        new.ht()
        new.penup()
        new.speed(0)
        new.color(random.choice(COLOR))
        new.shapesize(stretch_len=2)
        new.setheading(180)
        new.goto(x=random.randrange(280, 480, 40), y=random.randrange(-240, 280, 20))
        new.st()
        self.cars.append(new)

    def motion(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() <= -320:
                car.goto(x=random.randrange(280, 480, 40), y=random.randrange(-240, 280, 20))
