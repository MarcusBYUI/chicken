from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.scripting.handle_restart_action import HandleRestartAction
from game.casting.car import Car
from game.casting.log import Log
from random import  *

import time

class HandleLevelUp(Action):
    """
    An update action that handles HandleLevelUp of the chicken.
    
    The responsibility of HandleLevelUp is to handle the change in level of the chicken

    Attributes:
        _level_up (boolean): Whether or not the it is time to level up.
    """

    def __init__(self):
        """Constructs a new HandleLevelUp."""
        self._level_up = False
        self._keyboard_service = KeyboardService()
        self._action = HandleRestartAction(self._keyboard_service)
        

    def execute(self, cast, script):
        """Executes the HandleLevelUp action if the user qualifies for level up.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._level_up:

            self._check_level_up(cast)
            
            if self._level_up:
                self._prepare_levelup(cast, script)
                
        else:
            time.sleep(3)
            message = cast.get_last_actor("messages")
                
            message.set_text("")
            self._do_level_up(cast, script)


    
    def _check_level_up(self, cast):
        """Checks the position of the actor on the screen if it has gotten to the state where level up is needed.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        chicken = cast.get_first_actor("chicken")
        if chicken.get_position().get_y() == 50:
            self._level_up = True
        
                
    def _do_level_up(self, cast, script):
        """Actual level up is done since the actor(Chicken meets the requirement)
        """
        
        level = cast.get_first_actor("level")
        last_level = level.get_level()
        
        level.next_level()
        
        next_level = level.get_level()
        level.set_text(f"Level: {next_level}")
        
        chicken = cast.get_first_actor("chicken")

        chicken.set_position(Point(int(MAX_X/2), int(MAX_Y - 30)))
        
    
        car_rows = cast.get_actors("car")
        for rows in car_rows:
            rows.start_cars(randint(last_level - randint(1, 3), next_level))

        
        log_rows = cast.get_actors("log")
        for rows in log_rows:
            rows.start_logs(randint(last_level - randint(1, 3) ,next_level))
        
        self._level_up = False
        
        
        
        
    def _prepare_levelup(self, cast, script):
        """A message that prepares the user for a level up


        """
        if self._level_up:
            
            message = Actor()
            x = int(MAX_X / 2)
            y = int(10)
            position = Point(x, y)
            message.set_position(position)
            
            
            message.set_text("Level Completed!!, Brace for the Next Level")  
            message.set_font_size = 20
            
            
                
            cast.add_actor("messages", message)                
    
            self._level_up = True
        