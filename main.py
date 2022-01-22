from turtle_crossing_game.turtle_main import Turtle_Crossing_Game
from ping_pong.pong_main import Pong_Game
from hangman.hangman_main import Hangman_Game
from blackjack.blackjack_main import Blackjack_Game
from number_guessing_game.number_guessing_main import Number_Guessing_Game
from higher_lower_game.higher_lower_main import Higher_Lower_Game
from quiz_game.quizzler_main import Quizzler_Game
from snake.snake_main import Snake_Game
from turtle_race.race_main import Race_Game
from rps.rps_main import RPS

game_list = {1: Turtle_Crossing_Game,
             2: Pong_Game,
             3: Hangman_Game,
             4: Blackjack_Game,
             5: Number_Guessing_Game,
             6: Higher_Lower_Game,
             7: Quizzler_Game,
             8: Snake_Game,
             9: Race_Game,
             10: RPS}

game_option = int(input("1 for Turtle Crossing, 2 for Ping Pong, 3 for Hangman, 4 for Blackjack, 5 for Number "
                        "Guessing Game, 6 for Higher Lower Game, 7 for Quiz Game, 8 for Snake, 9 for Turtle Race, "
                        "10 for Rock Paper Scissors: "))

game_list[game_option]()
