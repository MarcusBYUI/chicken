from game.casting.actor import Actor
from game.shared.point import Point
from constants import *



class Level(Actor):
    """
    A record of game play levels. 
    
    The responsibility of Score is to keep track of the game level. It also displays itself at in the top banner

    Attributes:
        _level (int): The points earned in the game.
        _color (instance): color of level
        _position (int): position of the level on the screen
        set_text (int): level's text
        _font_size (int): level display font size
    """
    def __init__(self):
        super().__init__()
        self._level = 1
        self._color = GREEN
        self._position = Point(100, 10)
        self.set_text(f"level: {self._level}")
        self._font_size = 20
        
        
        

    def next_level(self):
        """Adds a level to the last level.
        
        """
        self._level += 1
        
    def get_level(self):
        
        return self._level
    
    def reset(self):
        self._level = 1