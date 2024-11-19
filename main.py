from player_resources import *
from items import *
from paths import *
from base_functions import *
from combat import *
from exploration import *
from enemy import *
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
        timeprint("All commands can be used by typing the letters in parentheses.")
    elif action == 'explore' or action == "e":
        you = explore()
    elif action == 'rest' or action == 'r':
        timeprint("You rest for a while.")
    elif action == 'test':
        you = combat(Enemy("bob",15,5,2),you)
    else:
        timeprint("That didn't work. Type (H)elp to see commands.")