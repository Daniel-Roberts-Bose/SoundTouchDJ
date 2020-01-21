"""
youtube_parser.py
Handles parsing youtube links into audio streams
@author Daniel Roberts
"""
from urllib.parse import urlparse


def parse_url(url):
    parse = urlparse(url)
    if parse.netloc != "www.youtube.com" and parse.netloc != "youtube.com":
        print("URL must be a youtube link")
        raise Exception("URLError")


class YoutubeParser:
    def __init__(self, url):
        parse_url(url)
        self.url = url

    def get_url(self):
        return self.url

