from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from random import *



class Banner(Actor):
    """
    A Banner is where the game score, game level and game messages are displayed

    Attributes:
        start position Point(int, int): The start x and y position of the banner.
        start position Point(int, int): The end x and y position of the banner.
        color: The color of the banner.

    """
    def __init__(self):
        super().__init__()
  
        #banner        
        start = Point(0, 0)
        end = Point(MAX_X, 40)
        self.set_position(start)
        self.set_end_position(end)
        self.set_color(BLACK)
        




    