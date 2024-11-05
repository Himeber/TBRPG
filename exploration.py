from base_functions import *
from mugging import *

def explore():
    global you
    timeprint("You decide to go exploring.")
    seed = rng()
    for i in random.randint(0,3):
        timeprint (". . .")
    if seed < 0.05:
        #mugging
        mug()
    elif seed < 0.1:
        #powerful enemy
        pass
    elif seed < 0.15:
        #nothing
        pass
    elif seed < 0.2:
        #toe stubbage
        pass
    elif seed < 0.25:
        #task
        pass
    elif seed < 0.3:
        #training
        pass
    elif seed < 0.5:
        #regular enemy
        pass
    elif seed < 0.6:
        #shop
        pass
    elif seed < 0.65:
        #fud
        pass
    elif seed < 0.75:
        #choice
        pass
    elif seed < 0.85:
        #bag of gold
        pass
    elif seed < 0.9:
        #dungeon entrance
        pass
    elif seed < 0.95:
        #chest
        pass
    else:
        #big chest
        pass