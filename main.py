"""
The main python script
@author Daniel Roberts
"""
import server
import speaker_communication
from song import Suggestions

if __name__ == "__main__":
    # global data structure for storing requests, this is a singleton
    suggestions = Suggestions.instance()

    # start the now playing listener and speaker communication
    speaker = speaker_communication.Speaker("localhost:8001")

    # start the flask server to handle incoming requests
    server.app.run()
