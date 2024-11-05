from base_functions import *
class Ability:
    def __init__(self,name,atk=0,heal=0,cost=0,special=None):
        self.name = name
        self.attack = atk
        self.heal = heal
        self.cost = cost
        self.special = special
    def __repr__(self):
        returner = str(f"""{self.name} - Costs {str(self.cost)} Mana
Deals {str(self.attack)}x damage
Heals for {str(self.heal)}x your attack""")
        if self.special != None:
            returner += f"\nSpecial: {self.special}"
        return str(returner)
    def __str__(self):
        return str(self.__repr__())
class Passive:
    def __init__(self,atk,hp,defence,mana):
        self.atk = atk
        self.hp = hp
        self.defence = defence
        self.mana = mana
    def __repr__(self):
        returner = ""
        if self.atk > 0:
            returner += f"+{str(self.atk)} ATK "
        if self.hp > 0:
            returner += f"+{str(self.hp)} HP "
        if self.defence > 0:
            returner += f"+{str(self.defence)} DEF "
        if self.mana > 0:
            returner += f"+{str(self.mana)} Mana"
        return returner
    def __str__(self):
        return self.__repr__()

class EnemyAbility:
    def __init__(self,name,damage,healing,priority,other = None):
        self.name = name
        self.dmg = damage
        self.heal = healing
        self.priority = priority
        self.other = other
    def __repr__(self) -> str:
        return str(f"{self.name} - Priority {self.priority}\n{line()}\nDamage: {str(self.dmg)}x attack stat\nHeals for {str(self.heal)}x attack stat\nSpecial: {str(self.other)}\n{line()}")