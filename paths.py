from base_functions import *
from abilities_spells import *

class Path:
    def __init__(self,name="",leveling = {

    }):
        self.name = name
        self.leveling = leveling
    
    def __repr__(self):
        returner = (str(f"""{line()}
Path of the {self.name}
{line()}"""))
        for level in self.leveling:
            skill = self.leveling[level]
            returner += f"\nLevel {str(level)}: {skill.name}"
        returner += "\n"
        returner += line()
        return returner
    
Student = Path("Student")
ApprenticeTable = {
    1 : Passive(0,0,0,5,0),
    2 : Ability("Mana Bolt",1.2,0,3),
    3 : Passive(0,0,0,0,2.5),
    4 : Passive(0,0,0,10,0),
    5 : Passive(0,0,0,0,5)
}
Apprentice = Path("Apprentice",ApprenticeTable)