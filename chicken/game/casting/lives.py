from game.casting.actor import Actor
from game.shared.point import Point
from constants import *




class Lives(Actor):
    """
    A record of Actors'(chicken) lives. 
    
    The responsibilty of the actor is to keep track of the actors live so it the end of the game can be managed.

    Attributes:
        _lives (int): The actors lives.
        _color (instance): color of live  text
        _position (int): position of the live  text on the screen
        set_text (int): live  text
        _font_size (int): live text display font size
    """
    def __init__(self):
        super().__init__()
        self._lives = CHICKENS_LIVES
        self._color = WHITE
        self._position = Point(0, 10)
        self.set_text(f"Lives: {self._lives}")
        self._font_size = 20
        
        
        

    def remove_live(self):
        """removes 1 from the actors live.
        
        Args:
            points (int): The points to add.
        """
        self._lives -= 1
        
    def get_lives(self):
        
        return self._lives