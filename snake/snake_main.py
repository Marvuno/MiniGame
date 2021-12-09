from turtle import Screen
from snake.player import Snake
from snake.food import Food
from snake.scoreboard import Scoreboard
from time import sleep


"""
Snake Game (Ver.2)
Changelog:
1) Rainbow Snake Mode removed (unpopular to players according to feedback)
2) Added new High Score System
    -> Added High Score
    -> High Score will keep updating forever
3) No more Game Over (removed)
    
Previous Versions:
Ver.1 
Changelog:
1) Rainbow Snake Mode available (Enable it yourself in player.py)

Known Bugs:
1) Quickly switching direction may result in GAME OVER (e.g. snake moving right, quickly turning up/down and then left.
2) Food may spawn inside the snake.
3) Rainbow Snake cannot retain its color in correct order.
4) Play the game at the given size. Do not go fullscreen.
5) There may be a slight mismatch between the snake and the wall at collision.
"""


def Snake_Game():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game = True
    while game:
        screen.update()
        sleep(0.075)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 5:
            food.ht()
            scoreboard.update()
            snake.grow()
            food = Food()

        # Detect collision with wall
        if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
            scoreboard.game_over()
            snake.reset()

        # Detect collision with tail
        for i in snake.segment:
            if snake.head.distance(i) < 10:
                scoreboard.game_over()
                snake.reset()

    screen.exitonclick()
