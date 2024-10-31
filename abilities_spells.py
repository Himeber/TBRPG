class Ability:
    def __init__(self,name,atk=0,heal=0,cost=0):
        self.name = name
        self.attack = atk
        self.heal = heal
        self.cost = cost
    
    def __repr__(self):
        return str(f"""{line()}
{self.name} - Costs {str(self.cost)} mana
{line()}
Doe""")
class Passive:
    def __init__(self,atk,hp,defence,mana):
        self.atk = atk
        self.hp = hp
        self.defence = defence
        self.mana = mana