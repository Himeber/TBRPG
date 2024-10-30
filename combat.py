from base_functions import *
def combat(enemy):
    global you
    cs()
    print(you)
    timeprint("You are entering combat with a " + enemy.name + "!")
    while enemy.hp > 0 and you.hp > 0:
        cs()
        print(you)
        timeprint("It's your turn.")
        action = strput("What would you like to do?")
        if action == "attack" or action == "a" or action == "atk":
            dmg = int(you.atk * (random.random() + 0.5) - enemy.defence)
            enemy.damage(dmg)
            timeprint("You attacked!")
            timeprint("You dealt " + str(dmg) + ".")

def bosscombat(enemy):
    pass