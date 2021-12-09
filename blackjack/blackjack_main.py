"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""
import blackjack.art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def Blackjack_Game():
    print(blackjack.art.logo)
    begin()


def begin():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        print("---------------------------------------------------------------------")
        play()
    else:
        pass


def final_score(my_cards, com_cards):
    print(f"Your cards: {my_cards}, final score: {sum(my_cards)}")
    print(f"Computer's final hand: {com_cards}, final score: {sum(com_cards)}")


def current_score(my_cards, com_cards):
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {com_cards[0]}")


# Convert 11 --> 1 and Double 11 scenario
def doubleA(my_cards, com_cards):
    if sum(my_cards) > 21:
        if 11 in my_cards:
            my_cards[my_cards.index(11)] = 1
    elif sum(com_cards) > 21:
        if 11 in com_cards:
            com_cards[com_cards.index(11)] = 1


def play():
    # User's Cards
    my_cards = []
    my_cards.append(cards[random.randint(0, 12)])
    my_cards.append(cards[random.randint(0, 12)])

    # AI's Cards
    com_cards = []
    com_cards.append(cards[random.randint(0, 12)])
    com_cards.append(cards[random.randint(0, 12)])

    # In Case of 2A start
    doubleA(my_cards, com_cards)

    current_score(my_cards, com_cards)
    compare(my_cards, com_cards)


# Blackjack
def compare(my_cards, com_cards):
    if sum(my_cards) == 21 and sum(com_cards) != 21:
        final_score(my_cards, com_cards)
        print("Blackjack! You win!")
        begin()
    elif sum(com_cards) == 21 and sum(my_cards) != 21:
        final_score(my_cards, com_cards)
        print("Blackjack! You lose.")
        begin()
    else:
        choice(my_cards, com_cards)


def choice(my_cards, com_cards):
    # If another card
    if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        my_cards.append(cards[random.randint(0, 12)])
        doubleA(my_cards, com_cards)
        current_score(my_cards, com_cards)

        # Busted
        if sum(my_cards) > 21:
            final_score(my_cards, com_cards)
            print("Busted. You lose.")
            begin()
            return
        choice(my_cards, com_cards)

    # User is Done
    else:
        # AI take card
        while (sum(com_cards) < 17):
            com_cards.append(cards[random.randint(0, 12)])

            # AI got busted
            if (sum(com_cards) > 21):
                if 11 in com_cards:
                    com_cards[com_cards.index(11)] = 1
                else:
                    final_score(my_cards, com_cards)
                    print("Computer got Busted. You Win! :P")
                    begin()

        # Result
        final_score(my_cards, com_cards)
        if (sum(my_cards) > sum(com_cards)):
            print("You win!")
            begin()
        elif (sum(my_cards) == sum(com_cards)):
            print("You draw.")
            begin()
        else:
            print("You lose.")
            begin()
