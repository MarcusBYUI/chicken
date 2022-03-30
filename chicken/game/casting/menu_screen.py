from tkinter import font
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import *



class Menu(Actor):
    """
    A road is where the chicken are to be able to cross

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def __init__(self):
        super().__init__()\
            
        self._start_game = False
        self._restart = False
        self._draw = True
        self._texts = []
        
        self._prepare_text()
        
        
        
    def _prepare_text(self):
                
        #Header
        text = Actor()
        text.set_text("Welcome To Chicken")
        text.set_font_size(45)
        text.set_color(YELLOW)
        position = Point(250, 30)
        text.set_position(position)
        
        self._texts.append(text)
        
        #Authors
        author = Actor()
        author.set_text("Author: Marcus Ojo-Osasere")
        author.set_font_size(20)

        position = Point(250, 100)
        author.set_position(position)
        
        self._texts.append(author)
        
        #Prompt
        prompt = Actor()
        prompt.set_text("Press Enter To Begin")
        prompt.set_font_size(20)
        prompt.set_color(YELLOW)

        position = Point(250, 200)
        prompt.set_position(position)
        
        self._texts.append(prompt)
        

    def set_draw(self, value):
        self._draw = value
        

    def get_draw(self):
        return self._draw
    
    
    def get_texts(self):
        return self._texts
    
    
    def add_game_over(self):
        prompt = Actor()
        prompt.set_text("Game Over")
        prompt.set_font_size(30)
        prompt.set_color(RED)

        position = Point(250, 250)
        prompt.set_position(position)
        
        self._texts.append(prompt)
        
        self.game_over = True
        
    
    def change_game_state(self, state):
        
        self._start_game = state
        
    def get_game_state(self):
        return self._start_game
    
    def set_restart(self, state):
        self._restart = state
        
    def restart_state(self):
        return self._restart

        

    