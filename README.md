hundred_prisoners
=================

This is an interactive framework for developing and testing solutions to
the 100 prisoners puzzle. The problem is as follows:

100 prisoners held captive by a group of cannibals. Each prisoner is
randomly inscribed with either True or False on the back of his head,
and they are then lined up. Each prisoner thus cannot see his own value,
but he can see the value of everyone in front of him in line, so the
last person in line can see 99 other values while the first person in
line can see no values. The cannibals proceed down the line from the
back to the front. Each prisoner can guess their value; if they are
wrong, they die. What strategy should the prisoners use to maximize
the number of survivors?

With this framework, you'll implement the strategy that the prisoners
use; each prisoner knows which number in line he is, the values of all
prisoners in front of him in line, what each prisoner behind him
guessed, and whether each prisoner behind him died (when a prisoner is
eaten, it gets ... loud). You have all the information necessary to
save a surprisingly large number of the prisoners, so each unnecessary
death is on your hands.

This is a slight modification of the original formulation seen at the
following link, with the main difference between that the colors blue
and red were replaced with the boolean values True and False, for ease
of interacting with them programmatically.

http://tierneylab.blogs.nytimes.com/2009/03/23/the-puzzle-of-100-hats/

Have at it!
