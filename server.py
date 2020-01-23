from flask import *
from song import Song
import requests, json, random

app = Flask(__name__)

# global data structure for storing requests
suggestions = []


# TODO: implement this later
def send_request_to_speaker(url):
    return url


def make_json(**kwargs):
    return json.dumps(dict(kwargs.items()))


@app.route('/')
def welcome():
    return "Welcome to the SoundTouchDJ app. To suggest a song please use the /suggest endpoint"


@app.route('/suggest', methods=['POST'])
def suggest():
    global suggestions
    song_name = request.args.get('name')
    artist = request.args.get('artist')
    url = request.args.get('url')
    request_id = random.getrandbits(128)
    try:
        new_suggestion = Song(song_name, artist, url, request_id)
        suggestions.append(new_suggestion)
        return make_json(status="success",
                         song_name=song_name,
                         artist=artist,
                         url=url,
                         request_id=request_id)
    except Exception as ex:
        return make_json(error='An exception occurred in parsing the suggested song URL',
                         exception=ex.__str__(),
                         song_name=song_name,
                         artist=artist,
                         url=url,
                         request_id=request_id)


@app.route('/queue', methods=['GET'])
def get_queue():
    # format the queue in a user friendly way
    song_list = []
    for item in suggestions:
        song_list.append(item.get_song())
    return make_json(queue=song_list)
