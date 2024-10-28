from base_functions import *
from abilities_spells import *

class Path:
    def __init__(self,name=""):
        self.name = name
        self.leveling = {

        }
    
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