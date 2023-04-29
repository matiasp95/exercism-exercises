import random, time

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Robot:
    def __init__(self):
        self.name = self.get_rand()
    def reset(self):
        self.name = self.get_rand()
        return self.name
    def get_rand(self):
        random.seed(None)
        return str(random.choice(chars) + random.choice(chars) + str(random.randint(100,999)))

# Set a seed
seed = "Totally random."

# Initialize RNG using the seed
random.seed(seed)

# Call the generator
robot = Robot()
name = robot.name

# Reinitialize RNG using seed
random.seed(seed)

# Call the generator again
robot.reset()
name2 = robot.name

print(name)
print(name2)