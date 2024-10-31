class Ability:
    def __init__(self,name,atk=0,heal=0,cost=0):
        self.name = name
        self.attack = atk
        self.heal = heal
        self.cost = cost
    def __repr__(self):
        return str(f"""{self.name} - Costs {str(self.cost)} Mana
Deals {str(self.attack)}x damage
Heals for {str(self.heal)}x your attack""")
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