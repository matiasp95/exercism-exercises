"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.
    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    def __init__(self, x_c, y_c, h_val = 3):
        self.x_coordinate = x_c
        self.y_coordinate = y_c
        self.health = h_val
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1
    def is_alive(self):
        return self.health > 0
    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    def collision_detection(self, other):
        pass

def new_aliens_collection(aliens):
    return [Alien(i[0],i[1]) for i in aliens]

Alien.total_aliens_created = 0
aliens = [Alien(-2, 6)]
Alien(3,4)
aliens.append(Alien(3, 5))
aliens.append(Alien(-5, -5))

tac_list = [alien.total_aliens_created for alien in aliens]
print(tac_list)
