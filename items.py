from base_functions import *
class Item:
    def __init__(self,name,slot,hp=0,defence=0,mana=0,matk=0,atk=0,special=None):
        self.name = name
        self.slot = slot
        self.hp = hp
        self.defence = defence
        self.mana = mana
        self.atk = atk
        self.special = special
        self.matk = matk
    def __repr__(self):
        returner = str(f"""{self.name} - {self.slot}
Defence: {str(self.defence)} | Attack: {str(self.atk)}
HP: {str(self.hp)} | Mana: {str(self.mana)}""")
        if self.special != None:
            returner += f"\nSpecial: {self.special}"
        return str(returner)
    
    def __str__(self):
        return str(self.__repr__())
    
class Chest:
    def __init__(self,name="Chest",contents=[],money = 0) -> None:
        self.contents = contents
        self.money = money
        self.name = name

def generateItem(makeStats=True,itemhp=0,itematk=0,itemdef=0,itemmana=0,itemmatk=0):
    pass

def generateChest(you,mult=1):
    scalar = you.level * mult * (random.random() + 0.5)
    scalar *= 5
    itemhp = 0
    itematk = 0
    itemdef = 0
    itemmana = 0
    itemmatk = 0
    muns = 0
    for i in range(scalar):
        randomized = rng()
        if randomized >= 0.9:
            muns += round(random.random() * 100,2)
        elif randomized >= 0.8:
            itemhp += int((random.random()+0.5) * 5)
        elif randomized >= 0.7:
            itematk += int((random.random()) * 5)
        elif randomized >= 0.6:
            itemdef += int((random.random()) * 3)
        elif randomized >= 0.5:
            itemmana += int((random.random()+0.5) * 5)
        elif randomized >= 0.4:
            itemmatk += int((random.random()+0.5) * 5)
        elif randomized >= 0.3:
            itemhp += 1
            itematk += 1
            itemdef += 1
            itemmana += 1
            itemmatk += 1
            muns += 1
        else:
            pass
    item = generateItem(False,itemhp,itematk,itemdef,itemmana,itemmatk)