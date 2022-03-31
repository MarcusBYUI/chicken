from game.scripting.action import Action
from game.shared.point import Point
import time


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        #chicken
        chicken = cast.get_first_actor("chicken")
        animation = chicken.get_animation()
        image = animation.next_image()
        pos = chicken.get_position()
        
        #menu screen
        menu = cast.get_first_actor("menu")
        texts = menu.get_texts()
        
        
        """checks if draw screen is on, which means its either the game is over or yet to start:
        if True: screen is drawn,
        else: Game is drawn
        """
        if menu.get_draw():
            
            #time.sleep(3)
            
            self._video_service.clear_buffer()
                
            self._video_service.draw_menu(texts)
            

                
            self._video_service.flush_buffer()
            
            
        else:
            
            #banner
            banner = cast.get_first_actor("banner")
            
            #road
            road = cast.get_first_actor("road")
          
            #river
            river = cast.get_first_actor("river")
   
            #lives
            lives = cast.get_first_actor("lives")
            
            #level
            level = cast.get_first_actor("level")
            
            #cars
            cars_list = cast.get_actors("car")
            
            #log
            log_list = cast.get_actors("log")


            
            #game meassages
            messages = cast.get_actors("messages")
            
        
        
            
            
            #Begin drawing------------------------------------------------------------------------------
            self._video_service.clear_buffer()
            #self._video_service._draw_grid()
            # banner drawing
            self._video_service.draw_shape(banner)
            
            
            #road drawing
            self._video_service.draw_shape(road, True)
            
            #river drawing
            self._video_service.draw_shape(river)
            
            
            
            #chicken drawing
            self._video_service.draw_image(image, pos)
            
            #car drawing
            for car in cars_list:
                cars = car.get_cars()
                self._video_service.draw_images(cars)
                
            #log drawing
            for log in log_list:
                logs = log.get_logs()
                self._video_service.draw_images(logs)
                
            
            
            #lives drawing
            self._video_service.draw_actor(lives)
            
            #level drawing
            self._video_service.draw_actor(level)
            
            #message drawing
            self._video_service.draw_actors(messages, True)
                
                    
                
                
            self._video_service.flush_buffer()
            #End drawing -----------------------------------------------------------------------