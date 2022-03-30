from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from random import *



class River(Actor):
    """
    A road is where the chicken are to be able to cross

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def __init__(self):
        super().__init__()
  
        #river
        start = Point(0, MAX_Y-320)
        end = Point(MAX_X, 125)
        self.set_position(start)
        self.set_end_position(end)
        self.set_color(BLUE)
        




    