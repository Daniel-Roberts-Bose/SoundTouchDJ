"""
speaker_communication.py
Contains code for dealing with speaker interaction
@author Daniel Roberts
"""
from song import Suggestions
from song import Song
from threading import Thread
from threading import Lock
from time import sleep
import requests
import util

# global data structure for storing requests, this is a singleton
suggestions = Suggestions.instance()


class Speaker:
    # Endpoint definitions
    post_play_audio_endpoint = "/speaker"  # for initiating playback
    get_now_playing_endpoint = "/nowPlaying"
    poll_interval = 5  # the polling interval in seconds

    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.thread = Thread(target=self.poll_speaker, args=(self.poll_interval,))
        self.running_lock = Lock()
        self.is_running = False
        self.start_listener()

    def start_listener(self):
        #  poll the speaker every half a second, if its playing a song, continue,
        #  else try and pop something from the queue. if the queue is empty, do nothing
        #  We don't need to lock here because this is happening during initialization
        self.is_running = True
        self.thread.start()

    def poll_speaker(self, interval):
        print("Polling loop BEGIN. Interval = %f" % interval)
        while util.perform_atomic_get(self.running_lock, self.get_is_running):
            # send a request to the speaker to see if we are currently playing,
            # if we are not, pop something from the queue and play it
            song = util.perform_atomic_get(suggestions.suggestions_lock, suggestions.pop_suggestion)
            print(song)
            sleep(interval)

    # must be called from a thread safe manner, using a lock
    def set_is_running(self, value):
        self.is_running = value

    # must be called from a thread safe manner, using a lock
    def get_is_running(self):
        return self.is_running
