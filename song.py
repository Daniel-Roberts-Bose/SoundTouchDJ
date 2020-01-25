"""
song.py
contains a class definition for the song data type
@author Daniel Roberts
"""
from youtube_parser import YoutubeParser
from collections import deque
import util


class Suggestions(object):
    __instance = None

    # static singleton creation method
    @classmethod
    def instance(cls):
        if cls.__instance is None:
            print("Creating new Suggestions instance")
            cls.__instance = cls.__new__(cls)
            cls.suggestions = deque([])  # an array of Song objects
        return cls.__instance

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    # logic for adding a suggestion to the array
    def add_suggestion(self, song_name, artist, url):
        request_id = util.make_random_request_id()
        try:
            new_suggestion = Song(song_name, artist, url, request_id)
            self.suggestions.append(new_suggestion)
            return util.make_json(status="success", song_name=song_name, artist=artist, url=url, request_id=request_id)
        except Exception as ex:
            return util.make_json(error='An exception occurred in parsing the suggested song URL',
                                  exception=ex.__str__(),
                                  song_name=song_name, artist=artist, url=url, request_id=request_id)

    # converts the suggestions array into json
    def get_suggestions(self):
        song_list = []
        for item in self.suggestions:
            song_list.append(item.get_song())
        return util.make_json(queue=song_list)

    def pop_suggestion(self):
        return self.suggestions.popleft() if len(self.suggestions) > 0 else None


class Song:
    def __init__(self, name, artist, url, req_id):
        self.name = name
        self.artist = artist
        # for now we only allow a youtube link, more to extend in the future
        youtube_parser = YoutubeParser(url)
        self.url = youtube_parser.get_url()

        # unique identifier
        self.req_id = req_id

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_url(self):
        return self.url

    def get_req_id(self):
        return self.req_id

    def get_song(self):
        ret = {"name": self.name, "artist": self.artist, "url": self.url}
        return ret
