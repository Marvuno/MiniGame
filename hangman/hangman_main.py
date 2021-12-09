import random
from hangman.words import word_list
from hangman.art import logo, stages


def Hangman_Game():
    chosen_word = random.choice(word_list)
    lives = 6
    print(logo)
    print(stages[lives])

    display = ['_'] * len(chosen_word)
    print(' '.join(display))
    count = len(chosen_word)

    while count > 0 and lives > 0:
        guess = input("\nGuess a letter: ").lower()
        print(f"'{guess}' is in the word.") if guess in chosen_word else print(f"'{guess}' is not in the word.")

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                count -= 1
            elif guess not in chosen_word:
                lives -= 1
                break
        print(stages[lives])
        print(' '.join(display))

    print(f"\nYou win! The word is {chosen_word}.") if lives > 0 else print(f"\nYou lose! The word is {chosen_word}.")
