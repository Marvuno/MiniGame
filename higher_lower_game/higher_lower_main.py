import random
import higher_lower_game.art
from higher_lower_game.game_data import data


def Higher_Lower_Game():
    second = -1
    final_score = 0
    first = random.randint(0, len(data) - 1)
    rand(first, second, final_score)


def rand(first, second, final_score):
    # Randomize game_data
    if second == first:
        second = random.randint(0, len(data) - 1)
    print(higher_lower_game.art.logo)
    print(f"Compare A: {data[first]['name']}, a {data[first]['description']}, from {data[first]['country']}")
    print(higher_lower_game.art.vs)
    print(f"Against B: {data[second]['name']}, a {data[second]['description']}, from {data[second]['country']}")

    # Determine answer and result
    confirm = input("Who has more followers? Type 'A' or 'B': ").upper()
    if ((data[first]['follower_count'] > data[second]['follower_count'] and confirm == 'A') or (
            data[first]['follower_count'] < data[second]['follower_count'] and confirm == 'B')):
        final_score += 1
        first = second
        rand(first, second, final_score)
    else:
        print(f"Your guess is incorrect. Your final score is {final_score}.")
