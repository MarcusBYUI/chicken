from game.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._video_service = video_service
        self._audio_service = audio_service
        

    def execute(self, cast, script):
        self._audio_service.load_sounds("chicken/assets/sounds")
        self._video_service.load_images("chicken/assets/images") 
        