"""Solution to Ellen's Alien Game exercise."""
def new_aliens_collection(positions):
    return list(map(lambda position: Alien(position[0], position[1]), positions ) )
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
    
    def __init__(self,x,y,health=3):
        self.health = health
        self.x_coordinate = x
        self.y_coordinate = y
        Alien.total_aliens_created += 1
    def hit(self):
        self.health -= 1
        
    def is_alive(self):
        if self.health > 0:
            return True
        else: return False
    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    def collision_detection(self,altro_alieno):
        return None