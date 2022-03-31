from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import *



class Car(Actor):
    """
    A Car is a list of cars moving in a particular direction

    Attributes:
        _cars (list): The number of cars on a lane.
        _level (int): The current level of the game
        _image (list): A list of car images
        _size(int): The car size
        _speed(int): The car speed in the specified direction
    """
    def __init__(self, speed, y_position,image, size, level=1):
        super().__init__()
        
        self._cars = []     
        self._level = level
        self._image = image
        self._size = size
          

        self._speed = speed
        self._prepare_cars(y_position)
        
    def _prepare_cars(self, y_position):
        """Begins a for loop that creates a list of cars for the specified lane y_position

        Args:
            y_position (int): the lane on the y axis
        """
                
        for i in range(0, MAX_X, CAR_GAP * self._gap(self._level)): 
            car = Actor()
            car.set_image(self._image[randint(0,5)])
            car.set_size(self._size)
            x = i
            y = y_position
            position = Point(x, y)
            car.set_position(position)
            
            self._cars.append(car)
            
            
            
    def _gap(self, level):
        if level % 2 == 0:
            return int(level/2)
        else:
            return level     
        
           
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        
        for car in self._cars:
            x = (car.get_position().get_x() - (self._speed * self._level)) % MAX_X
            y = car.get_position().get_y()
            #car.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            
            car.set_position(Point(x, y))
        
    def get_cars(self):
        return self._cars
    
    def stop_cars(self):
        self._speed = 0
        
    def start_cars(self, speed):
        if speed <= 0:
            speed = 1
        self._speed = speed


    