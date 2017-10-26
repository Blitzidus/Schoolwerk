from random import *


def monepolyworp(start):
    doubleCounter = start
    dice1 = randrange(1, 6)
    dice2 = randrange(1, 6)
    if dice1 == dice2:
        if doubleCounter == 2:
            print("{} + {} = {} (rechtstreeks naar de gevangenis)".format(dice1, dice2, dice1 + dice2))
        else:
            print("{} + {} = {} (dubbel)".format(dice1, dice2, dice1 + dice2))
            doubleCounter += 1
            monepolyworp(doubleCounter)
    else:
        print("{} + {} = {}".format(dice1, dice2, dice1 + dice2))


monepolyworp(0)
