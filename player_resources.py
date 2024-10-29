from base_functions import *
from paths import (Student)
from abilities_spells import *
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
        self.abilities = [] 
        self.helmet = None
        self.hand1 = None
        self.hand2 = None
        self.chest = None
        self.legs = None
        self.boots = None
        self.gloves = None
        self.ring1 = None
        self.ring2 = None
        self.pendant = None

    def __repr__(self):
        return str(f"""{line()}
{self.name} - Level {str(self.level)} {self.path.name}
{line()}
{str(self.xp)}/{str(self.xpneeded)} to the next level
HP: {str(self.hp)}/{str(self.maxhp)} | Mana: {str(self.mana)}/{str(self.maxmana)}
Attack: {str(self.atk)} | Defence : {str(self.defence)}
{line()}""")

    def refresh(self):
        abilites = []
        hp = self.basehp
        attack = self.baseatk
        defence = self.basedefence
        mana = self.basemana
        for i in self.path.leveling:
            if i <= self.level:
                skill = self.path.leveling[i]
                if isinstance(skill,Ability):
                    abilites.append(skill)
                elif isinstance(skill,Passive):
                    hp += skill.hp
                    attack += skill.atk
                    defence += skill.defence
                    mana += skill.mana
                else:
                    pass
        if self.ring1:
            pass
        if self.ring2:
            pass
        if self.boots:
            pass
        if self.chest:
            pass
        if self.gloves:
            pass
        if self.helmet:
            pass
        if self.pendant:
            pass
        if self.legs:
            pass

player = Player("bob")
player.refreshAbilities()