from game.scripting.action import Action


class UnloadAssetsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script):
        self._video_service.unload_images()