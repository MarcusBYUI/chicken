from game.scripting.action import Action
from game.casting.sound import Sound
from constants import *
from random import  *

class MoveCarAction(Action):
    
    def __init__(self, audio_service):
        super().__init__()
        self._audio_service = audio_service
        self._car_horn = Sound(CAR_HORN)
            
        
    def execute(self, cast, script):
        """Executes the move_next on the car action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """        
        self._move_car(cast)

    def _move_car(self, cast):
        """calls the move.next() method that handles the movement of the car
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        rate = randint(1,5)
        cars = cast.get_actors("car")
        chicken = cast.get_first_actor("chicken")  
        menu = cast.get_first_actor("menu")
        
        
        for car in cars:
            car.move_next()
        
        if rate == 1 and menu.get_draw() == False and chicken.get_position().get_y() in range(MAX_Y - 150, MAX_Y):
            self._audio_service.play_sound(self._car_horn)
            
        
