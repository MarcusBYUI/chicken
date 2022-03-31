from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from random import *



class River(Actor):
    """A River is where the the logs float pass

        Attributes:
            start position Point(int, int): The start x and y position of the banner.
            start position Point(int, int): The end x and y position of the banner.
            color: The color of the banner."""
        
    def __init__(self):
        super().__init__()
  
        #river
        start = Point(0, MAX_Y-320)
        end = Point(MAX_X, 125)
        self.set_position(start)
        self.set_end_position(end)
        self.set_color(BLUE)
        




    