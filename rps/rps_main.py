# This entrypoint file to be used in development. Start by reading README.md
from rps.RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from rps.RPS import player
from unittest import main


# play(player, human, 100)
# play(player, quincy, 1000)
# play(player, abbey, 1000)
# play(player, kris, 1000)
# play(player, mrugesh, 1000)


def RPS():
    opponents_dict = {"human": human,
                      "quincy": quincy,
                      "abbey": abbey,
                      "kris": kris,
                      "mrugesh": mrugesh}

    print("Hello! This is Wincy, a Rock Paper Scissors Expert AI.\nYou may choose the opponent against me below.")
    opponent = input(
        "Opponents:\nHuman (YOU)\nQuincy (Weakest)\nKris (Weak)\nMrugesh (Strong)\nAbbey (Strongest)\n").lower()
    number_of_games = int(input("How many games to run/play?(Recommend 1000 games for bots): "))
    play(player, opponents_dict[opponent], number_of_games)

# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)


# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)
