from game.scripting.action import Action


class UnloadAssetsAction(Action):

    def __init__(self,audio_service, video_service):
        self._audio_service = audio_service
        
        self._video_service = video_service

    def execute(self, cast, script):
        self._video_service.unload_images()
        self._audio_service.unload_sounds()
        