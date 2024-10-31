from player_resources import *
from items import *
from paths import *
from base_functions import *
from combat import *
cs()
global you
name = strput("What's your name?").title()
cs()
you = Player(name)
