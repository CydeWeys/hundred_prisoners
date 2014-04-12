#!/usr/bin/python

import random, copy

# These are your input parameters. The default values are sane, though feel
# free to adjust to play around. n = 3 makes for a good base case.
n = 100 # The number of prisoners
ratio = 0.5 # The probability that a prisoner's value is True

###
# This is the function you need to implement.
#
# i is the number of this prisoner, from 0 to n-1.
# dead is a list of booleans for whether or not each previous prisoner died.
# declared is a list of booleans that each previous prisoner declared.
#     For both of these lists, the result of the most recent prisoner to go is
#     the last element, and these lists are both empty for the first prisoner to go.
# ahead is a list of booleans for all prisoners that the current prisoner can see.
#     For this list, the next prisoner to go is the first element, and the last
#     prisoner to go will have an empty ahead list.
# Returns: The boolean that the current prisoner declares.
def prisoner_action(i, dead, declared, ahead):
    # Your implementation goes here. All prisoners declaring themselves True is
    # going to kill a lot of them. Can you do better?
    return True


# Don't change any code beyond this line. This is the bookkeeping of the simulation.
def run_simulation():
    prisoners = [random.random() < ratio for r in range(n)]
    ahead = copy.copy(prisoners)
    dead = []
    declared = []
    num_dead = 0

    # The game loop
    for i in range(n):
        ahead.pop(0)
        declaration = prisoner_action(i, dead, declared, ahead)
        declared.append(declaration)
        dead.append(declaration != prisoners[i])
        if (declaration != prisoners[i]):
            num_dead += 1

    print('Out of {0} prisoners, you killed {1}.'.format(n, num_dead))
    if (num_dead > 1 or (True in dead[1:])):
        print('You can do better than that!')
    else:
        print('Great job! You found the right algorithm!')

run_simulation()
