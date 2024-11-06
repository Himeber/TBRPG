from base_functions import *
from paths import *
from abilities_spells import *
from items import *

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
        self.matk = 10
        self.basematk = 10
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
        self.inv = [None,None,None,None,None,None,None,None,None]
        self.moneys = 0.00

    def __repr__(self):
        return str(f"""{line()}
{self.name} - Level {str(self.level)} {self.path.name}
{line()}
{str(self.xp)}/{str(self.xpneeded)} to the next level
HP: {str(self.hp)}/{str(self.maxhp)} | Mana: {str(self.mana)}/{str(self.maxmana)}
Attack: {str(self.atk)} | Defence : {str(self.defence)} | Magic Attack: {str(self.matk)}
{line()}""")

    def refresh(self):
        abilites = []
        hp = self.basehp
        attack = self.baseatk
        defence = self.basedefence
        mana = self.basemana
        matk = self.basematk
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
                    matk += skill.matk
                else:
                    pass
        if self.ring1:
            hp += self.ring1.hp 
            attack += self.ring1.atk
            defence += self.ring1.defence
            mana += self.ring1.mana
            matk += self.ring1.matk
        if self.ring2:
            hp += self.ring2.hp 
            attack += self.ring2.atk
            defence += self.ring2.defence
            mana += self.ring2.mana
            matk += self.ring2.matk
        if self.boots:
            hp += self.boots.hp 
            attack += self.boots.atk
            defence += self.boots.defence
            mana += self.boots.mana
            matk += self.boots.matk
        if self.chest:
            hp += self.chest.hp 
            attack += self.chest.atk
            defence += self.chest.defence
            mana += self.chest.mana
            matk += self.chest.matk
        if self.gloves:
            hp += self.gloves.hp 
            attack += self.gloves.atk
            defence += self.gloves.defence
            mana += self.gloves.mana
            matk += self.gloves.matk
        if self.helmet:
            hp += self.helmet.hp 
            attack += self.helmet.atk
            defence += self.helmet.defence
            mana += self.helmet.mana
            matk += self.helmet.matk
        if self.pendant:
            hp += self.pendant.hp 
            attack += self.pendant.atk
            defence += self.pendant.defence
            mana += self.pendant.mana
            matk += self.pendant.matk
        if self.legs:
            hp += self.legs.hp 
            attack += self.legs.atk
            defence += self.legs.defence
            mana += self.legs.mana
            matk += self.legs.matk
        self.maxhp = hp
        self.atk = attack
        self.defence = defence
        self.maxmana = mana
        self.matk = matk
        for skill in abilites:
            if skill not in self.abilities:
                self.abilities.append(skill)

    def showabilites(self):
        print(line())
        for skill in self.abilites:
            timeprint(skill)
            print(line())

    def use(self,ability):
        dmg = self.matk * ability.attack
        dmg = dmg * (random.random() + 0.5)
        dmg = int(dmg)
        heal = self.matk * ability.heal
        heal = heal * (random.random() +0.5)
        heal = int(heal)
        if self.maxhp - self.hp < heal:
            heal = self.maxhp - self.hp
        return dmg,heal