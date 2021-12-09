from turtle import Turtle, Screen
from random import randint


def Race_Game():
    screen = Screen()
    screen.setup(width=500, height=400)
    bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtle = []
    y_coordinate = -100
    race = False

    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(x=-230, y=y_coordinate)
        y_coordinate += 30
        all_turtle.append(new_turtle)

    if bet:
        race = True

    while race:
        for turtle in all_turtle:
            turtle.forward(randint(0, 10))
            if turtle.xcor() >= 230:
                winner = turtle.pencolor()
                race = False

    if bet == winner:
        print("You win!")
    else:
        print(f"You lose! The winner is the {winner} turtle.")

    screen.bye()
