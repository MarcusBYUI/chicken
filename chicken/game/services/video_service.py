from distutils.log import debug
import pyray
from constants import *
import pathlib
import os



class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
        self._textures = {}
        

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(GREEN.to_tuple())

        
        if self._debug == debug:
            
            pass
            #self._draw_grid()
    
    def draw_actor(self, actor, centered=False, menu=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset
            
        pyray.draw_text(text, x, y, font_size, color)
        
    
        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor, centered)
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(MAX_X, MAX_Y, CAPTION)
        pyray.set_target_fps(FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""

            
        for x in range(0, MAX_X, CELL_SIZE):
            pyray.draw_line(x, 0, x, MAX_Y, pyray.BLACK)
            
 
        
    def draw_shape(self, actor, lanes=False):

        """Draws the shapes for the given actor on the screen.

        Args:
            actors (Actor): An instancvce of actor to draw.
        """ 
        x1 = actor.get_position().get_x()
        y1 = actor.get_position().get_y()
        x2 = actor.get_end_position().get_x()
        y2 = actor.get_end_position().get_y()
        color = actor.get_color().to_tuple()
        
        pyray.draw_rectangle(x1, y1, x2, y2, color) 
        
        
        if lanes:
        #Draw lanes
            for i in range(5, MAX_X, 35):
                pyray.draw_line_ex(pyray.Vector2(i, MAX_Y-117), pyray.Vector2(i+10, MAX_Y-117), 4, pyray.WHITE); 
                pyray.draw_line_ex(pyray.Vector2(i, MAX_Y-77), pyray.Vector2(i+10, MAX_Y-77), 4, pyray.WHITE); 
         
         
    def draw_menu(self, actors):
        """Draws the game menu.

        Args:
            actor (list):  List of texts to be displayed

        """ 
        pyray.draw_rectangle(0,0, MAX_X, MAX_Y, pyray.BLACK) 
        for actor in actors:
            self.draw_actor(actor)

        
        
    
    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)
    
    
    def draw_image(self, image, position, menu=False):

        """Draws the image for the given actor on the screen.

        Args:
            actor (instance): An of actor to draw.
        """ 
        filepath = image.get_filename()
        texture = self._textures[filepath]
        x = position.get_x()
        if menu:
            y = position.get_y() - 50
        else:
            y = position.get_y()
        raylib_position = pyray.Vector2(x, y)
        scale = image.get_scale()
        rotation = image.get_rotation()
        tint = self._to_raylib_color(Color(255,255,255)) 
        pyray.draw_texture_ex(texture, raylib_position, rotation, scale, tint)
        
    def draw_images(self, actors, centered=False):
        """Draws the images for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_image(actor.get_image(), actor.get_position())
        
    def _to_raylib_color(self, color):
        r, g, b, a = color.to_tuple()
        return pyray.Color(r, g, b, a)
    
    def load_images(self, directory):
        filepaths = self._get_filepaths(directory, [".png", ".gif", ".jpg", ".jpeg", ".bmp"])
        for filepath in filepaths:
            if filepath not in self._textures.keys():
                texture = pyray.load_texture(filepath)
                self._textures[filepath] = texture
                
    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = directory + '/' + file
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filepaths.append(filename)
        return filepaths  
    
    def unload_images(self):
        for texture in self._textures.values():
            pyray.unload_texture(texture)
        self._textures.clear()