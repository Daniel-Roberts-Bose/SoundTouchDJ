"""
youtube_parser.py
Handles parsing youtube links into audio streams
@author Daniel Roberts
"""
from urllib.parse import urlparse
from urllib.request import urlopen


def parse_url(url):
    # check the url is actually valid
    parse = urlparse(url)
    if parse.netloc != "www.youtube.com" and parse.netloc != "youtube.com":
        print("URL must be a youtube link")
        raise Exception("URLError")

    # next check we can actually ping the url
    ret_code = urlopen(url).getcode()
    if ret_code != 200:
        print("URL returned non 200 status code")
        raise Exception("URLError")


class YoutubeParser:
    def __init__(self, url):
        parse_url(url)
        self.url = url

    def get_url(self):
        return self.url

