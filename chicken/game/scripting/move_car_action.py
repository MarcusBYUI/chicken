from game.scripting.action import Action

class MoveCarAction(Action):
    def execute(self, cast, script):
        """Executes the grow trail action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """        
        self._move_car(cast)

    def _move_car(self, cast):
        """Add segments to grow the trail of the cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cars = cast.get_actors("car")
        for car in cars:
            car.move_next()
