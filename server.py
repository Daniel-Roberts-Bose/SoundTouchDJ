"""
server.py
Contains the main flask server code for handling requests
@author Daniel Roberts
"""

from flask import *
from song import Suggestions

app = Flask(__name__)

# global data structure for storing requests, this is a singleton
suggestions = Suggestions.instance()


@app.route('/')
def welcome():
    return "Welcome to the SoundTouchDJ app. To suggest a song please use the /suggest endpoint"


@app.route('/suggest', methods=['POST'])
def suggest():
    global suggestions
    song_name = request.args.get('name')
    artist = request.args.get('artist')
    url = request.args.get('url')
    # TODO: Need to add some thread safety here
    return suggestions.add_suggestion(song_name, artist, url)


@app.route('/queue', methods=['GET'])
def get_queue():
    global suggestions
    return suggestions.get_suggestions()
