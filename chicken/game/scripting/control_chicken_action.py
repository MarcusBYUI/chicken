from constants import *


from game.scripting.action import Action
from game.shared.point import Point


class ControlChickenAction(Action):
    """
    An input action the Chicken.
    
    The responsibility of ControlChickenAction is to get the direction and move chicken in that direction.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlChickenAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        
        self._direction = Point(0, 0)
        


    def execute(self, cast, script):
        """Executes the control chicken action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        chicken = cast.get_first_actor("chicken")  
        menu = cast.get_first_actor("menu")
               
        
        
        # left
        if menu.get_game_state():
            if self._keyboard_service.is_key_down('left'):
                if chicken.get_position().get_x() <= 0:
                    self._direction = Point(0, 0)
                    
                else:
                    self._direction = Point(-10, 0)
            
            # right
            if self._keyboard_service.is_key_down('right'):
                if chicken.get_position().get_x() >= MAX_X -20:
                    self._direction = Point(0, 0)               
                else:
                    self._direction = Point(10, 0)
            
            # up
            if self._keyboard_service.is_key_down('up'):
                if chicken.get_position().get_y() <= MAX_Y - 350:
                    self._direction = Point(0, 0)               
                else:
                    self._direction = Point(0, -CELL_SIZE)
            

            chicken = cast.get_first_actor("chicken")
            chicken.set_velocity(self._direction)
            self._direction = Point(0, 0)
        
        