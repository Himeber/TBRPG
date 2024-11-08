from base_functions import *
def combat(enemy):
    global you
    turn = True
    cs()
    print(you)
    timeprint("You are entering combat with a " + enemy.name + "!")
    while enemy.hp > 0 and you.hp > 0:
        cs()
        print(you)
        timeprint("It's your turn.")
        turn = True
        while turn:
            action = strput("What would you like to do?").lower()
            if action == "attack" or action == "a" or action == "atk":
                dmg = int(you.atk * (random.random() + 0.5) - enemy.defence)
                enemy.damage(dmg)
                timeprint("You attacked!")
                timeprint("You dealt " + str(dmg) + ".")
                turn = False
            elif "cast" in action:
                caster = action[5:]
                for i in you.abilities:
                    if caster == i.name:
                      if you.mana >= i.cost:
                        dmg,heal = you.use(i)
                        dmg -= enemy.defence
                        cost = i.cost
                        if dmg > 0:
                            timeprint(f"You dealt {dmg} damage to the {enemy.name}.")
                            enemy.damage(dmg)
                        if heal > 0:
                            timeprint(f"You healed for {heal} HP.")
                            you.hp += heal
                        if cost > 0:
                            you.mana -= cost
                        turn = False
                if i not in you.abilities:
                    timeprint(f"You cannot use {caster} because you do not know it.")
            elif action == "l" or "list":
                for i in you.abilities:
                    timeprint(f"{i.name} - Costs {i.cost} mana")
            else:
                timeprint("Use '(a)ttack' to attack, or use 'cast ___' to cast an ability.")
                timeprint("Use '(l)ist' to look at available abilities.")
        timeprint(f"It's the {enemy.name}'s turn.")
        dmg = enemy.atk * (random.random() + 0.5)
        dmg -= you.defence
        dmg = int(dmg)
        if dmg < 0:
            dmg = 0
        timeprint(f"The {enemy.name} dealt {dmg} to you.")
        you.hp -= dmg
    if you.hp <= 0:
        timeprint("You have died.")
    if enemy.hp <= 0:
        timeprint(f"The {enemy.name} has died.")
def bosscombat(enemy):
    pass
