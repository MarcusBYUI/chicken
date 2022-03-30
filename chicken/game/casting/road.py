from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from random import *



class Road(Actor):
    """
    A road is where the chicken are to be able to cross

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def __init__(self):
        super().__init__()       
        x = 300
        y = 30
        start = Point(0, MAX_Y-155)
        end = Point(MAX_X, 120)
        self.set_position(start)
        self.set_end_position(end)
        self.set_color(BLACK)
        
        
    



    