from constants import *
from game.casting.sound import Sound


from game.scripting.action import Action
from game.shared.point import Point


class HandleRestartAction(Action):
    """
    An input action that handles restart action.
    
    The responsibility of HandleRestartAction is to get the input from the Spacebar to restart the game.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self,audio_service, keyboard_service):
        """Constructs a new HandleRestartAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
        self._game_sound = Sound(GAME_PLAY_SOUND)
        
      

    def execute(self, cast, script):
        """Executes the handle restart action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        menu = cast.get_first_actor("menu")

        if self._keyboard_service.is_key_down('space'):
            if not menu.get_game_state():
                #start game
                menu.set_draw(False)
                self._audio_service.stop_sound(self._game_sound)            
                self._game_sound.set_volume(0.5)
                self._audio_service.play_sound(self._game_sound)
                menu.change_game_state(True)
            
            elif menu.get_draw():
                # restart action
                
                menu.set_restart(True)
         
                   

            
        
        

