"""
speaker_communication.py
Contains code for dealing with speaker interaction
@author Daniel Roberts
"""
from song import Suggestions

# global data structure for storing requests, this is a singleton
suggestions = Suggestions.instance()


class Speaker:
    # Endpoint definitions
    post_play_audio_endpoint = "/speaker"
    get_now_playing_endpoint = "/nowPlaying"

    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.start_listener()

    def start_listener(self):
        pass

    # TODO: implement this
    def request_new_song(self, url):
        pass

    # TODO: this function should be a callback for now playing notifications
    def handle_now_playing(self):
        pass
