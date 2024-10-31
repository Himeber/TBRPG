from base_functions import *

def explore():
    global you
    timeprint("You decide to go exploring.")
    seed = rng()
    for i in random.randint(0,3):
        timeprint (". . .")
    if seed < 0.05:
        #mugging
        timeprint("You see a man waking across the road.")
        mugging = ["sprints at you with","throws a paper airplane at you containing","ignores the laws of physics and teleports in front of you with"]
        weapon = ["a hammer","a stick","a sign that says 'GIM LIBER'","your wallet","a bomb","ten pounds of mustard","a particularly large sock"]
        mood = ["angrily","doesn't","from halfway in the floor","cheerfully","nonexistently"]
        timeprint(str(f"He {random.choice(mugging)} {random.choice(weapon)} and {random.choice(mood)} asks for your money."))
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