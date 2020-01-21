"""
song.py
contains a class definition for the song data type
@author Daniel Roberts
"""
from youtube_parser import YoutubeParser


class Song:
    def __init__(self, name, artist, url):
        self.name = name
        self.artist = artist
        # for now we only allow a youtube link, more to extend in the future
        youtube_parser = YoutubeParser(url)
        self.url = youtube_parser.get_url()

    def __str__(self):
        return "Song: %s, Artist: %s, URL: %s" % (self.name, self.artist, self.url)

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_url(self):
        return self.url
