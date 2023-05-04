import math
import random

class Character:
    def __init__(self):
        self.strength = self.random_stat_gen()
        self.dexterity = self.random_stat_gen()
        self.constitution = self.random_stat_gen()
        self.intelligence = self.random_stat_gen()
        self.wisdom = self.random_stat_gen()
        self.charisma = self.random_stat_gen()
        self.hitpoints = 10 + modifier(self.constitution)

    def random_stat_gen(self):
        #Roll a dice 4 times between 1 and 6
        rolls = [random.randint(1,6) for i in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)
    
    def ability(self):
        return random.choice([x for x in vars(self).values()])
def modifier(const):
    return math.floor((const - 10)/2)

print(Character().ability())