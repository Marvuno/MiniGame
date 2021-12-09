from turtle import Screen
from ping_pong.paddle import Paddle
from ping_pong.ball import Ball
from ping_pong.scoreboard import Scoreboard
import time


def Pong_Game():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(height=600, width=800)
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Key bindings
    screen.listen()
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")
    screen.onkeypress(l_paddle.up, 'w')
    screen.onkeypress(l_paddle.down, 's')

    game = True
    while game:
        screen.update()
        time.sleep(0.02)
        ball.move()

        # Collision on walls
        if ball.ycor() <= -280 or ball.ycor() >= 280:
            ball.bounce_y()
        # Collision on paddles
        elif (ball.distance(l_paddle) <= 50 and ball.xcor() <= -330) or \
                (ball.distance(r_paddle) <= 50 and ball.xcor() >= 330):
            ball.bounce_x()
            # Increase move speed
            ball.x_move *= 1.1
            ball.y_move *= 1.1
            ball.play += 1

        # Left lost
        if ball.xcor() <= -400:
            scoreboard.right_win()
            ball.reset_position()
        # Right lost
        if ball.xcor() >= 400:
            scoreboard.left_win()
            ball.reset_position()

    screen.exitonclick()
