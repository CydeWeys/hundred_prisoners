#!/usr/bin/python

import random, copy

# The number of iterations of the game to play
# Make this larger for a more accurate simulation, at the expense of running time.
n = 10000 

###
# This is the function you need to implement.
#
# num_remaining is the number of cards left in the deck; it is a value between 2 and 52.
# revealed_cards is an array of all of the cards that have been revealed so far this round.
#                The end of the array is the most recently revealed card.
# reds_remaining and blacks_remaining are self-explanatory.
# Returns: The boolean that indicates whether you wish to bet on the next card or not.
def redblack_action(num_remaining, revealed_cards, reds_remaining, blacks_remaining):
    # Your implementation goes here. The default implementation is to always bet, which
    # should yield a win rate of 50%. Can you do better?
    return True


# Don't change any code beyond this line. This is the bookkeeping of the simulation.
def run_simulation():
    won = 0
    for i in range(n):
        # Creates a deck of 26 red and 26 black cards and randomly shuffles it.
        cards = [True for r in range(26)] + [False for r in range(26)]
        for c in range(0, 50):
            swap_place = random.randint(c+1, 51)
            tmp = cards[swap_place]
            cards[swap_place] = cards[c]
            cards[c] = tmp
        revealed_cards = []

        while len(cards) > 0:
            # The last card is always played.
            if len(cards) == 1:
                if cards[0]:
                    won += 1
                break
            player_bet = redblack_action(len(cards), revealed_cards, cards.count(True), cards.count(False))
            card = cards.pop(0)
            revealed_cards.append(card)
            if player_bet:
                if card:
                    won += 1
                break

    print('Out of {0} games, you won {1}, for a win % of {2:.2f}.'.format(n, won, 100.00 * float(won) / float(n)))
    print('But can you do better?')


run_simulation()
