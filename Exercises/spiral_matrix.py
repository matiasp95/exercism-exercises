
DIRECTION_TO_COORDS ={
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

def spiral_matrix(size):
    max_val = size**2
    matrix = [[0 for i in range(size)] for j in range(size)]
    start_coord = (0,0)
    init_degree = Degrees(90)
    
    for t in range(max_val):
        if t == 0:
            matrix[start_coord[0]][start_coord[1]] = t+1
            start_coord = (start_coord[0]+DIRECTION_TO_COORDS[init_degree.get_direction()][0], start_coord[1]+DIRECTION_TO_COORDS[init_degree.get_direction()][1])
            continue
        if(((start_coord[0]+1 == size and init_degree.get_direction() == "S") or 
            (start_coord[0]-1 == -1 and init_degree.get_direction() == "N")) or 
            ((start_coord[1]+1 == size and init_degree.get_direction() == "E") or 
            (init_degree.get_direction() == "W" and start_coord[1]-1 == -1))):
            matrix[start_coord[0]][start_coord[1]] = t+1
            init_degree.rotate_90_degrees()
            start_coord = (start_coord[0]+DIRECTION_TO_COORDS[init_degree.get_direction()][0], start_coord[1]+DIRECTION_TO_COORDS[init_degree.get_direction()][1])
            continue
        try:
            if((init_degree.get_direction() == "N" and matrix[start_coord[0]-1][start_coord[1]] != 0) or 
                (init_degree.get_direction() == "S" and matrix[start_coord[0]+1][start_coord[1]] != 0) or
                (init_degree.get_direction() == "E" and matrix[start_coord[0]][start_coord[1]+1] != 0) or
                (init_degree.get_direction() == "W" and matrix[start_coord[0]][start_coord[1]-1] != 0)):
                matrix[start_coord[0]][start_coord[1]] = t+1
                init_degree.rotate_90_degrees()
                start_coord = (start_coord[0]+DIRECTION_TO_COORDS[init_degree.get_direction()][0], start_coord[1]+DIRECTION_TO_COORDS[init_degree.get_direction()][1])
                continue
        except IndexError:
            pass
        matrix[start_coord[0]][start_coord[1]] = t+1
        start_coord = (start_coord[0]+DIRECTION_TO_COORDS[init_degree.get_direction()][0], start_coord[1]+DIRECTION_TO_COORDS[init_degree.get_direction()][1])
    return matrix


class Degrees():
    def __init__(self, angle):
        self.angle = angle%360

    def get_direction(self):
        if self.angle == 0:
            return "N"
        elif self.angle == 90:
            return "E"
        elif self.angle == 180:
            return "S"
        elif self.angle == 270:
            return "W"
    def rotate_90_degrees(self):
        self.angle = (self.angle+90)%360


spiral_matrix(0)