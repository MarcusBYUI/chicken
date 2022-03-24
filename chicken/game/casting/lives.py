from game.casting.actor import Actor
from game.shared.point import Point
from constants import *




class Lives(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned.
    It contains methods for adding and getting points. Client should use get_text() to get a string representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._lives = 3
        self._color = WHITE
        self._position = Point(0, 10)
        self.set_text(f"Lives: {self._lives}")
        self._font_size = 20
        
        
        

    def remove_live(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._lives -= 1
        
    def get_lives(self):
        
        return self._lives