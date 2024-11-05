from base_functions import *
def mug():
    timeprint("You see a man walking across the road.")
    mugging = ["sprints at you with","throws a paper airplane at you containing","ignores the laws of physics and teleports in front of you with"]
    weapon = ["a hammer","a stick","a sign that says 'GIM LIBER'","your wallet","a bomb","ten pounds of mustard","a particularly large sock","a \"World's Greatest Mugger\" mug"]
    mood = ["angrily","doesn't","from halfway in the floor","cheerfully","nonexistently"]
    timeprint(str(f"He {random.choice(mugging)} {random.choice(weapon)} and {random.choice(mood)} asks for your money."))
    timeprint(f"He took ${str(you.money /2)}.")
    you.money /= 2