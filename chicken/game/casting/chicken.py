from constants import *
from game.casting.actor import Actor
from game.shared.point import Point


class Chicken(Actor):
    """
    A Chicken is an actor that is being controlled in the game, it inherits from the actor class
    
    The responsibility of Chicken is to be moved by the player.

    Attributes:
        _prepare_body (func): The number of points the collision is worth.
        _animation (instance): An instance of the Animation class holding images of the chicken
        _size: the size of the chicken
        
    """
    def __init__(self, animation, size):
        super().__init__()
        self._prepare_body()
        self._animation = animation
        self._size = size
        


    def _prepare_body(self):
        """Prepares the body of the chicken
        """

        self._font_size = 30
        x = int(MAX_X / 2)
        y = int(MAX_Y - 30)
        position = Point(x, y)
        self._position = position
        
    def get_animation(self):
        """Gets the chiken's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_size(self):
        """Gets the chickens's size.
        
        Returns:
            An sixe of the chicken.
        """
        return self._size
    