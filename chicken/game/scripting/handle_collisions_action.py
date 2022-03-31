from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.casting.car import Car
from game.casting.log import Log
from game.casting.lives import Lives
from game.casting.image import Image
from game.scripting.control_chicken_action import ControlChickenAction
from random import *




import time

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collide with their own segments, or the segments of it's opponent, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._counter = 0
        self._keyboard_service = KeyboardService()
    
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:

            self._handle_collision(cast)
            lives = cast.get_first_actor("lives") 
            #deduct live and start to run game over sequence before the next game loop
            if self._is_game_over:  
                lives.remove_live()
                lives.set_text(f"Lives: {lives.get_lives()}") 
                
                if lives.get_lives() <= 0:
                    self._handle_game_over(cast, script)  
                else:
                    self._handle_life_loss(cast, script) 
            
            
        else: 
            #first loop after the game over sequence
            #If user has lives: game restarts
            #else: its game over
            lives = cast.get_first_actor("lives") 
            
            if lives.get_lives() <= 0:
                self._restart(cast, script)
                
            else:
                self._continue(cast, script)
                
                
                
                


    
    def _handle_collision(self, cast):
        """Handles the collisions sequence.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        car_rows = cast.get_actors("car")
        car_base_row = car_rows[2]
        car_mid_row = car_rows[1]
        car_top_row = car_rows[0]
        
        self.check_car_collision(car_base_row, cast, 250)
        self.check_car_collision(car_mid_row, cast, 290)
        self.check_car_collision(car_top_row, cast, 330)
        
            
        
        log_rows = cast.get_actors("log")
        base_row = log_rows[2]
        mid_row = log_rows[1]
        top_row = log_rows[0]
        
        if self._is_game_over:
                
            
            return
            
        else:
                
            chicken = cast.get_first_actor("chicken") 
        
            if chicken.get_position().get_y() == 170:
                self._is_game_over = True
            self.check_log_collision(base_row, cast, 170)
            
            
            if chicken.get_position().get_y() == 130:
                self._is_game_over = True
            self.check_log_collision(mid_row, cast, 130)
            
            
            if chicken.get_position().get_y() == 90:
                self._is_game_over = True
            self.check_log_collision(top_row, cast, 90)
            
        
            
            if self._is_game_over:
                animation = chicken.get_animation()
                animation.set_boom(True)
                

                
    def check_log_collision(self, row, cast, y):   
        """works on colision between the chicken and the log on a particule y axis, which is also the same as the position of the logs in that lane

        Args:
            row (int): the row/lane of the log
            cast (Cast): The cast of Actors in the game.
            y (int): y axis of the log
        """
        chicken = cast.get_first_actor("chicken")         
        log_list = row.get_logs()
        
        for log in log_list:
            
            if chicken.get_position().get_y() == y and chicken.get_position().get_x() in range(log.get_position().get_x()-10, log.get_position().get_x()+50):
                chicken.set_position(Point(log.get_position().get_x() + 17, y))
                self._is_game_over = False
                if chicken.get_position().get_x() <= 0:
                    self._is_game_over = True
                    
                 
                
                
    def check_car_collision(self, row, cast, y):  
        """works on colision between the chicken and the car on a particule y axis, which is also the same as the position of the car in that lane

        Args:
            row (int): the row/lane of the car
            cast (Cast): The cast of Actors in the game.
            y (int): y axis of the car
        """ 
        chicken = cast.get_first_actor("chicken")         
        car_list = row.get_cars()
        
        for car in car_list:
            
            if chicken.get_position().get_y() == y and chicken.get_position().get_x() in range(car.get_position().get_x() - 20, car.get_position().get_x() + 40):
                self._is_game_over = True 
                animation = chicken.get_animation()
                animation.set_boom(True)
                  
            
        
                
    def _restart(self, cast, script):
        """When the game is over, this would be the method running in the game loop.
        It takes the cast and script as parameters and delays for about 3 sec for the user to see the boom.png of the chicken before
        drawing the game over screen.
        There is an if statement that checks if the user has pressed the spacebar to restart the game.
        
        

        Args:
            cast (Cast): The cast of Actors in the game.

            script (Script): The script of Actions in the game.

        """
        menu = cast.get_first_actor("menu")
        
        chicken = cast.get_first_actor("chicken")
        chicken.set_position(Point(int(MAX_X/2), int(MAX_Y - 30)))
        
        if self._counter < 1:
            time.sleep(3)
            self._counter = 1
        menu.set_draw(True)
        
        
        
        



    
        #checks for input  
        if menu.restart_state():
            animation = chicken.get_animation()
            animation.set_boom(False)

            level = cast.get_first_actor("level")
            level.next_level()
            
            
            
            cast.remove_group("lives")
            
            cast.add_actor("lives", Lives())
            
            
            next_level = 1
            level.set_text(f"Level: {next_level}")
            
            
            
            
        
                        
            car_rows = cast.get_actors("car")
            for rows in car_rows:
                rows.start_cars(randint(1,3))

            
            log_rows = cast.get_actors("log")
            for rows in log_rows:
                rows.start_logs(randint(1,3))
            
            
            menu.set_draw(False)
            menu.change_game_state(True)
            menu.set_restart(False)
            self._counter = 0

            self._is_game_over=False

            
        else:    pass    
        
        
    def _handle_game_over(self, cast, script):
        """Adds the game over text to the menu screen, stops the cars and sets _is_game_over to true
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        

        if self._is_game_over:
            

            
            
            # message.set_text("Game Over (Press Spacebar to Start again.)")
            menu = cast.get_first_actor("menu")
            #Adding the gameover text
            menu.add_game_over()
            
            car_rows = cast.get_actors("car")
            for rows in car_rows:
                rows.stop_cars()

            
            log_rows = cast.get_actors("log")
            for rows in log_rows:
                rows.stop_logs()
            
  
            

            self._is_game_over = True


    def _handle_life_loss(self, cast, script):
        """Shows the restart message.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        

        if self._is_game_over:

            message = Actor()
            x = int(MAX_X / 2)
            y = int(10)
            position = Point(x, y)
            message.set_position(position)
            message.set_font_size = 20
            
            
            
            message.set_text("Your Chicken Lost A Life, Restarting In 2 seconds")  
            
                
            cast.add_actor("messages", message) 
            
            

            
            self._is_game_over = True
            
    def _continue(self, cast, script):
        
        """delays for 2 sec and continues the game as a result of the fact that the players still has lives left
        """
        time.sleep(2)
        message = cast.get_last_actor("messages")
        message.set_text("")
        
        chicken = cast.get_first_actor("chicken")
        animation = chicken.get_animation()
        animation.set_boom(False)         
        
        
        chicken = cast.get_first_actor("chicken")
        if chicken.get_position().get_y() < 211:
            chicken.set_position(Point(int(MAX_X / 2), 210))
    
        elif chicken.get_position().get_y() < 370:
            chicken.set_position(Point(int(MAX_X/2), int(MAX_Y - 30)))
        self._is_game_over=False






            