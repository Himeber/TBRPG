from player_resources import *
from items import *
from paths import *
from base_functions import *
from combat import *
cs()
global you
name = strput("What's your name?").title()
you = Player(name)
while True:
    cs()
    print(you)
    action = strput("What would you like to do?").lower()
    if action == "help" or action == "h":
        timeprint("Possible actions:")
        timeprint("(H)elp")
        timeprint("(E)xplore")
        timeprint("(R)est")
        timeprint("(C)haracter")
        timeprint("All commands can be used by typing the letters in parentheses.")
    elif action == 'explore' or "e":
        explore()
    elif action == 'rest' or 'r':
        timeprint("You rest for a while.")