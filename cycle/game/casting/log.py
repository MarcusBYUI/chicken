from tkinter import font
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import *



class Log(Actor):
    """
    A is a floater on the stream that the chicken can climb on

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def __init__(self, speed, y_position, level=1):
        super().__init__()
        
        self._logs = []       

        self._speed = speed
        self._prepare_logs(y_position)
        self.level = level
        
        
    def _prepare_logs(self, y_position):
        for i in range(20, MAX_X, CELL_SIZE*5):
            log = Actor()
            log.set_text("---")
            log.set_font_size(CELL_SIZE)
            log.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            x = i
            y = y_position
            position = Point(x, y)
            log.set_position(position)
            
            self._logs.append(log)
            
        
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        
        for log in self._logs:
            x = (log.get_position().get_x() - (self._speed * self.level)) % MAX_X
            y = log.get_position().get_y()
            #log.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            
            log.set_position(Point(x, y))
        
    def get_logs(self):
        return self._logs
    
    def stop_logs(self):
        self._speed = 0