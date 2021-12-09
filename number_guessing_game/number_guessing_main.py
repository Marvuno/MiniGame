import random
import number_guessing_game.art

MODE = {'easy': 10, 'medium': 8, 'hard': 5}


def Number_Guessing_Game():
    print(number_guessing_game.art.logo)
    print("""Welcome to the Number Guessing Game! I am thinking of a number between 1 and 100.""")
    begin()


def begin():
    num = random.randint(1, 100)
    # Choose Difficulty
    diff = input("Choose a difficulty. Type 'easy' / 'medium' / 'hard': ").lower()
    # In case user type wrongly
    while diff != 'easy' and diff != 'medium' and diff != 'hard':
        diff = input("Choose a difficulty. Type 'easy' / 'medium' / 'hard': ")
    # Basic text
    attempt = MODE[diff]
    print(f"You have {attempt} attempts remaining to guess the number.")
    play(attempt, num)


def text(attempt, num):
    print("Guess again.")
    attempt -= 1
    print(f"You have {attempt} attempts remaining to guess the number.\n")
    play(attempt, num)


# Playing the game
def play(attempt, num):
    # Game over
    if (attempt == 0):
        print("You ran out of attempts. You lose.")
        print(f"The answer is {num}.")
        again()
    # Make a guess
    guess = int(input("Make a guess: "))
    while (guess < 1 or guess > 100):
        guess = int(input("The guess should be within 1 - 100: "))
    if (guess < num):
        print("Too low.")
        text(attempt, num)
    elif (guess > num):
        print("Too high.")
        text(attempt, num)
    else:
        print("You have successfully guessed the number!")
        again()


def again():
    # Sustainable
    if (input("Type 'y' to play again or 'n' to quit. ") == 'y'):
        begin()
    else:
        return
