from base_functions import *

class Enemy:
    def __init__(self,hp,atk,defence,xp):
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.xpreward = xp
    def attack(self,target):
        damage = self.atk
        damage = int(damage * (random.random()+0.5))
        damage = int(damage - target.defence)
        return damage
    def damage(self,damage):
        self.hp -= int(damage)
class Boss(Enemy):
    def __init__(self, hp, atk, defence, xp, abilities, rotation):
        super().__init__(hp, atk, defence, xp)
        self.abilities = abilities
        self.rotation = rotation