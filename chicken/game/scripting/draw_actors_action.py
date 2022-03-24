from game.scripting.action import Action


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
        lives = cast.get_first_actor("lives")
        level = cast.get_first_actor("level")

        cars_list = cast.get_actors("car")
        log_list = cast.get_actors("log")


        chicken = cast.get_first_actor("chicken")
        messages = cast.get_actors("messages")
        

        self._video_service.clear_buffer()
        #self._video_service._draw_grid()
        self._video_service.draw_actor(chicken)
        for car in cars_list:
            cars = car.get_cars()
            self._video_service.draw_actors(cars)
            
        for log in log_list:
            logs = log.get_logs()
            self._video_service.draw_actors(logs)
        
        

        self._video_service.draw_actor(lives)
        self._video_service.draw_actor(level)

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()