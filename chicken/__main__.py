from game.casting.cast import Cast
from game.casting.lives import Lives
from game.casting.level import Level
from game.casting.chicken import Chicken
from game.casting.car import Car
from game.casting.log import Log
from game.scripting.script import Script
from game.scripting.control_chicken_action import ControlChickenAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_level_up import HandleLevelUp
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.scripting.move_car_action import MoveCarAction
from constants import *

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("chicken", Chicken())
    cast.add_actor("lives", Lives())
    cast.add_actor("level", Level())
    
    #car lane 1
    cast.add_actor("car", Car(2, CAR_LANE_ONE))
    #car lane 1
    cast.add_actor("car", Car(1, CAR_LANE_TWO))
    #car lane 1
    cast.add_actor("car", Car(3, CAR_LANE_THREE))
    
    #Water Log
    cast.add_actor("log", Log(2, LOG_LANE_THREE))
    cast.add_actor("log", Log(1, LOG_LANE_TWO))
    cast.add_actor("log", Log(3, LOG_LANE_ONE))
    
    
    
   
    # start the game
    keyboard_service = KeyboardService() 
    video_service =  (VideoService())

    script = Script()
    script.add_action("input", ControlChickenAction(keyboard_service))
    
    script.add_action("update", MoveActorsAction())
    script.add_action("update", MoveCarAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", HandleLevelUp())
    
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()