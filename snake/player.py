from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.x_coordinate = 20
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment()
            self.segment[i].goto(x=self.x_coordinate, y=0)
            self.x_coordinate -= 20

    def grow(self):
        position = self.segment[-1].pos()
        self.add_segment()
        self.segment[-1].goto(position)

    def add_segment(self):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.speed(0)
        self.segment.append(new)

    def move(self):
        self.segment[-1].goto(self.head.pos())
        self.segment.insert(1, self.segment.pop())
        self.segment[0] = self.segment[1]
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segment:
            seg.goto(x=1000, y=1000)
        self.head.goto(x=1000, y=1000)
        self.segment.clear()
        self.x_coordinate = 20
        self.create_snake()
        self.head = self.segment[0]
