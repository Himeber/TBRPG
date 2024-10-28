from base_functions import *
from paths import (Student)
class Spellbook:
    def __init__(self,name=""):
        self.name = name
        self.abilites = {

        }

    def addability(self,ability):
        self.abilites[ability.name] = ability

class Player:
    def __init__(self,name):
        self.name = name
        self.path = Student
        self.hp = 100
        self.maxhp = 100
        self.atk = 10
        self.defence = 0
        self.mana = 100
        self.maxmana = 100
        self.basehp = 100
        self.baseatk = 10
        self.basedefence = 0
        self.basemana = 100
        self.xp = 0
        self.xpneeded = 1
        self.level = 0
        self.spellbook = Spellbook()
    
    def __repr__(self):
        return str(f"""{line()}
{self.name} - Level {str(self.level)} {self.path.name}
{line()}
{str(self.xp)}/{str(self.xpneeded)} to the next level
HP: {str(self.hp)}/{str(self.maxhp)} | Mana: {str(self.mana)}/{str(self.maxmana)}
Attack: {str(self.atk)} | Defence : {str(self.defence)}
{line()}""")
player = Player("bob")
timeprint(player)