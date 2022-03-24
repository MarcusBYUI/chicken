from game.scripting.action import Action

class MoveLogAction(Action):
    def execute(self, cast, script):
        """Executes the grow trail action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """        
        self._move_log(cast)

    def _move_log(self, cast):
        """Add segments to grow the trail of the cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        logs = cast.get_actors("log")
        for log in logs:
            log.move_next()
