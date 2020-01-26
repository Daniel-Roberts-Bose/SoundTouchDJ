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
        error_count = 0
        while util.perform_atomic_get(self.running_lock, self.get_is_running) and error_count < 10:
            # send a request to the speaker to see if we are currently playing,
            address = self.ip_address + self.get_now_playing_endpoint
            resp = requests.get(address)

            play_status = util.get_now_playing_play_status(resp)
            if play_status is None:
                error_count += 1
            else:
                # If we get a good response, check if we are playing or stopped

                # If we are not playing, start a new song, if we have something in the queue
                song = util.perform_atomic_get(suggestions.suggestions_lock, suggestions.pop_suggestion)
                if song is not None:
                    pass

            sleep(interval)

    # must be called from a thread safe manner, using a lock
    def set_is_running(self, value):
        self.is_running = value

    # must be called from a thread safe manner, using a lock
    def get_is_running(self):
        return self.is_running
