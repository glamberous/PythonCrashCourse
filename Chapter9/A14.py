
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        roll_result = randint(1, self.sides)
        print("Rolling " + str(self.sides) + "-sided die: " + str(roll_result))

die = Die()
die_10 = Die(10)
die_20 = Die(20)

for count in range(10):
    die.roll_die()

for count in range(10):
    die_10.roll_die()

for count in range(10):
    die_20.roll_die()

