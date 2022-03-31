from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from random import *



class Road(Actor):
    """A Road is where the cars pass by and the chiken tries to cross

        Attributes:
            start position Point(int, int): The start x and y position of the banner.
            start position Point(int, int): The end x and y position of the banner.
            color: The color of the banner."""
    def __init__(self):
        super().__init__()       
        x = 300
        y = 30
        start = Point(0, MAX_Y-155)
        end = Point(MAX_X, 120)
        self.set_position(start)
        self.set_end_position(end)
        self.set_color(BLACK)
        
        
    



    