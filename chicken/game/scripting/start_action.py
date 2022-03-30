from constants import *


from game.scripting.action import Action
from game.shared.point import Point


class StartAction(Action):
    """
    An input action that controls Cycle One.
    
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
        
        


    def execute(self, cast, script):
        """Executes the control chicken action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        menu = cast.get_first_actor("menu")
        
        
        
        # left
        if self._keyboard_service.is_key_down('enter'):
            menu.set_draw(False)     
            
            
        