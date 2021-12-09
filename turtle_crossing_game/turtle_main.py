from turtle_crossing_game.player import Player
from turtle_crossing_game.car import Car
from turtle_crossing_game.scoreboard import Scoreboard
from turtle import Screen
import time
import random


def Turtle_Crossing_Game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("white")
    screen.tracer(0)
    screen.listen()

    player = Player()
    car = Car()
    scoreboard = Scoreboard()
    screen.onkey(player.move, 'w')
    screen.onkey(player.cheater, "Tab")  # Cheat

    game = True
    while game:
        screen.update()
        time.sleep(0.05)
        car.motion()

        # Car spawning
        random_chance = random.randint(1, 10)
        if random_chance == 1:

            # Car spawn cap
            for _ in range(1):
                if len(car.cars) <= 10 * scoreboard.level:
                    car.create()

        # Collision with car
        for c in car.cars:
            if c.distance(player) < 20:
                scoreboard.lost()
                game = False

        # Next level
        if player.ycor() >= 300:
            player.advance()
            scoreboard.level_up()

            # Increase game difficulty
            car.speed += 1

    screen.exitonclick()
