"""
This project is dedicated to FreeCodeCamp Paper-Scissors-Rock Certification Project. 3 out of 5 implemented models are used and the AI should achieve >60% win rate against the four other opponents.
Model 1 -- Smart: Counter the countermeasure of the opponent.
Model 2 -- Rarity (not used): Play the counter of the opponent's least used play.
Model 3 -- Counter (not used): Find AI's most used play, then counter it.
Model 4 -- Pattern: Find out the pattern for the opponent and play against it.
Model 5 -- Markov: Develop a long markov chain to play intelligently.
Score: Sum(a * j) for each model.
"""
import numpy as np


def score():
    for j in range(len(method)):
        if method[j]() == opponent_history[-1]:
            a = 0
        elif (method[j]() == "P" and opponent_history[-1] == "R") or (
                method[j]() == "R" and opponent_history[-1]) == "S" or (
                method[j]() == "S" and opponent_history[-1] == "P"):
            a = 1
        else:
            a = -1
        strategy[j] += (a * i)


# Model 1
def smart():
    return ideal_response[ideal_response[my_history[-1]]]


# Model 2
def rarity():
    last_ten = opponent_history[-10:]
    least_frequent = ideal_response[min(set(last_ten), key=last_ten.count)]
    return least_frequent


# Model 3
def counter():
    my_twenty_five = my_history[-25:]
    my_frequent = ideal_response[ideal_response[max(set(my_twenty_five), key=my_twenty_five.count)]]
    return my_frequent


# Model 4
def pattern():
    similarity = 0
    last_hundred = opponent_history[-100:]
    last_ten = last_hundred[:10]
    for j in range(10, len(last_hundred), 10):
        cnt = 0
        new_ten = last_hundred[j - 10:j]
        for s in range(10):
            if last_ten[s] == new_ten[s]:
                cnt += 1
        if cnt >= 8:
            similarity += 1
        last_ten = new_ten
    if similarity >= 8:
        return True


# Model 5
def markov():
    last_three = "".join(opponent_history[-3:])
    last_four = "".join(opponent_history[-4:])
    if last_four in play_order.keys():
        play_order[last_four] += 1
    else:
        play_order[last_four] = 1

    potential_plays = [
        last_three + "R",
        last_three + "P",
        last_three + "S",
    ]

    for j in potential_plays:
        if j not in play_order.keys():
            play_order[j] = 0

    prediction = max(potential_plays, key=lambda key: play_order[key])[-1:]
    return ideal_response[prediction]


play_order = {}
ideal_response = {'P': 'S', 'S': 'R', 'R': 'P'}
win_pattern = []
opponent_history = ['P', 'R', 'S', 'R', 'P'] * 2
my_history = ['S', 'P', 'R', 'P', 'S'] * 2
strategy = [0, 0]
method = [smart, markov]  # Model 1 & 4
i = 1


def player(prev_play):
    global i, win_pattern, strategy, play_order, opponent_history, my_history

    # Reset
    if i % 1000 == 0:
        win_pattern = []
        opponent_history = ['P', 'R', 'S', 'R', 'P'] * 2
        my_history = ['S', 'P', 'R', 'P', 'S'] * 2
        strategy = [0, 0]
        play_order = {}
    # Soft Reset for Markov
    elif strategy[1] > strategy[0] and i % 200 == 0:
        win_pattern = []
        play_order = {}
    # Find Pattern
    elif i % 100 == 0:
        if pattern():
            if len(win_pattern) == 0:
                win_pattern.extend([ideal_response[answer] for answer in opponent_history[-10:]])
            else:
                win_pattern = ([ideal_response[answer] for answer in opponent_history[-10:]])

    # Scoring Models
    opponent_history.append(prev_play) if prev_play in ['P', 'R', 'S'] else opponent_history.append('P')
    score()
    if len(win_pattern) > 0:
        guess = win_pattern[i % 10]
    else:
        guess = method[np.argmax(strategy)]()
    my_history.append(guess)
    i += 1
    return guess
