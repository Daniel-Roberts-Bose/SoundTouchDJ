from flask import *
from song import Song
app = Flask(__name__)

# global data structure for storing requests
suggestions = []


# TODO: implement this later
def send_request_to_speaker(url):
    return url


@app.route('/')
def welcome():
    return "Welcome to the SoundTouchDJ app. To suggest a song please use the /suggest endpoint"


@app.route('/suggest', methods=['POST'])
def suggest():
    global suggestions
    song_name = request.args.get('name')
    artist = request.args.get('artist')
    url = request.args.get('url')
    try:
        new_suggestion = Song(song_name, artist, url)
        suggestions.append(new_suggestion)
    except Exception:
        abort(500)
        abort(Response("Could not parse song/url"))
    return "Thank you for your suggestion, the song with url %s has been queued" % url


@app.route('/queue', methods=['GET'])
def get_queue():
    # format the queue in a user friendly way
    ret = ""
    for item in suggestions:
        print(item)
        ret += item.__str__() + '\n'
    return ret
