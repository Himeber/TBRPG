from base_functions import *
from enemy import *
from combat import *

def explore(you):
    timeprint("You decide to go exploring.")
    seed = rng()
    for i in range(random.randint(0,3)):
        timeprint (". . .")
    if seed < 0.05:
        #mugging
        timeprint("You see a man walking across the road.")
        mugging = ["sprints at you with","throws a paper airplane at you containing","ignores the laws of physics and teleports in front of you with"]
        weapon = ["a hammer","a stick","a sign that says 'GIM LIBER'","your wallet","a bomb","ten pounds of mustard","a particularly large sock","a \"World's Greatest Mugger\" mug"]
        mood = ["angrily","doesn't","from halfway in the floor","cheerfully","nonexistently"]
        timeprint(str(f"He {random.choice(mugging)} {random.choice(weapon)} and {random.choice(mood)} asks for your money."))
        timeprint(f"He took ${str(you.money /2)}.")
        you.money /= 2
    elif seed < 0.1:
        #powerful enemy
        enemy = generate_enemy(you,1.5)
        timeprint("You stumble upon an old camp.")
        timeprint("There are signs of fighting and dried blood.")
        timeprint(f"Suddenly, a {enemy.name} bursts out of the forest and ambushes you!")
        combat(you,enemy)
    elif seed < 0.15:
        #dungeon entrance
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
        enemy = generate_enemy(you)
        enemy2 = enemy
        enemy3 = enemy
        timeprint("You are traveling through the forest.")
        timeprint(f"There's a group of enemies up ahead.")
        timeprint(f"There seems to be a {enemy.name}, an {enemy2.name}, and an {enemy3.name}.")
        timeprint(f"You decide to take them on one by one.")
        combat(you,enemy)
        combat(you,enemy2)
        combat(you,enemy3)
        timeprint("Exhausted, you find a chest in the center of the camp.")
        #chest here
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
    return you