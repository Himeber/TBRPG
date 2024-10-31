class Item:
    def __init__(self,name,slot,hp=0,defence=0,mana=0,atk=0,special=None):
        self.name = name
        self.slot = slot
        self.hp = hp
        self.defence = defence
        self.mana = mana
        self.atk = atk
        self.special = special
    
    def __repr__(self):
        returner = str(f"""{self.name} - {self.slot}
Defence: {str(self.defence)} | Attack: {str(self.atk)}
HP: {str(self.hp)} | Mana: {str(self.mana)}""")
        if self.special != None:
            returner += f"\nSpecial: {self.special}"
        return str(returner)
    
    def __str__(self):
        return str(self.__repr__())