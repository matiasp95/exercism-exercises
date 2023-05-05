# Globals for the directions
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)
MOVE_DICT={
    ("R",EAST): SOUTH,
    ("L",EAST): NORTH,
    ("R",WEST): NORTH,
    ("L",WEST): SOUTH,
    ("R",SOUTH): WEST,
    ("L",SOUTH): EAST,
    ("R",NORTH): EAST,
    ("L",NORTH): WEST,
}

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def move(self, instructions):
        for i in instructions:
            if (i,self.direction) in MOVE_DICT:
                self.direction = MOVE_DICT[(i,self.direction)]
            else:
                self.coordinates = (self.coordinates[0]+self.direction[0], self.coordinates[1]+self.direction[1])
    
r = Robot(NORTH,0,0)
def translate_coords_to_direction(tup):
    if tup == EAST:
        return "EAST"
    elif tup == WEST:
        return "WEST"
    elif tup == SOUTH:
        return "SOUTH"
    elif tup == NORTH:
        return "NORTH"
    
print("Current Coordinates:",r.coordinates)
print("Current Direction:",translate_coords_to_direction(r.direction))
r.move("RRAAARAALAA")
print("Rotating right, then right again, 3 advances in this direction, rotate right, two advances, rotate left, advance twice")
print("Current Coordinates:",r.coordinates)
print("Current Direction:",translate_coords_to_direction(r.direction))
