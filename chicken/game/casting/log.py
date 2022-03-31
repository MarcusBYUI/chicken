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
        _logs (list): The number of logs on a lane.
        _level (int): The current level of the game
        _image (list): A list of car images
        _size(int): The car size
        _speed(int): The log speed in the specified direction
        
    """
    def __init__(self, speed, y_position, image, size, level=1):
        super().__init__()
        
        self._logs = []       
        self._image = image
        self._size = size
        self._speed = speed
        self._level = level
        
        self._prepare_logs(y_position)
        
        
    def _prepare_logs(self, y_position):
        for i in range(20, MAX_X, CELL_SIZE*5 *(self._level)):
            log = Actor()
            log.set_image(self._image[randint(0,2)])
            log.set_size(self._size)
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
            x = (log.get_position().get_x() + (self._speed * self._level)) % MAX_X
            y = log.get_position().get_y()
            #log.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            
            log.set_position(Point(x, y))
        
    def get_logs(self):
        return self._logs
    
    def stop_logs(self):
        self._speed = 0
        
    def start_logs(self, speed):
        if speed <= 0:
            speed = 1    
        self._speed = speed
