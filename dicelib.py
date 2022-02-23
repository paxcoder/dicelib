import random
##it's the lib which will be used as our random number generator.
##let's make a dice def which then could be called by a python program
def dice():
    roll = random.randint(1,6)
    return roll