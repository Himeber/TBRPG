from base_functions import *

class Enemy:
    def __init__(self,name,hp,atk,defence,xp="calc"):
        self.hp = hp
        self.maxhp = hp
        self.name = name
        self.atk = atk
        self.defence = defence
        self.xpreward = xp
        if self.xpreward == "calc":
            self.xpreward = self.maxhp/5 + self.atk*1.5 + self.defence*2
            self.xpreward = self.xpreward * (random.random() + 0.5)
            self.xpreward = int(self.xpreward)
        self.goldreward = self.maxhp/2+self.atk*2+self.defence*3
        self.goldreward + self.goldreward * (random.random() + 0.5)
        self.goldreward = round(self.goldreward,2)
    def attack(self,target):
        damage = self.atk
        damage = int(damage * (random.random()+0.5))
        damage = int(damage - target.defence)
        return damage
    def damage(self,damage):
        self.hp -= int(damage)
    def __repr__(self):
        return f"""{line()}
{self.name} - {str(self.hp)}/{str(self.maxhp)} HP
{line()}"""
class Boss(Enemy):
    def __init__(self,name, hp, atk, defence, xp, abilities, rotation):
        super().__init__(name,hp, atk, defence, xp)
        self.abilities = abilities
        self.rotation = rotation
