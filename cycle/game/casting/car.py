from tkinter import font
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import *



class Car(Actor):
    """
    A road is where the chicken are to be able to cross

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def __init__(self, speed, y_position, level=1):
        super().__init__()
        
        self._cars = []     
        self.level = level
          

        self._speed = speed
        self._prepare_cars(y_position)
        
    def _prepare_cars(self, y_position):
        def gap(level):
                if level % 2 == 0:
                    return int(level/2)
                else:
                    return level
        for i in range(20, MAX_X, CELL_SIZE* 2 * gap(self.level)):
            car = Actor()
            car.set_text("=")
            car.set_font_size(CELL_SIZE)
            car.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            x = i
            y = y_position
            position = Point(x, y)
            car.set_position(position)
            
            self._cars.append(car)
            
            
            
        
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        
        for car in self._cars:
            x = (car.get_position().get_x() - (self._speed * self.level)) % MAX_X
            y = car.get_position().get_y()
            #car.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            
            car.set_position(Point(x, y))
        
    def get_cars(self):
        return self._cars
    
    def stop_cars(self):
        self._speed = 0
