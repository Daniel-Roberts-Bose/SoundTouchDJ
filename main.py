"""
The main python script
@author Daniel Roberts
"""
import server
import speaker_communication
from song import Suggestions
import signal
import sys
import util

# global data structure for storing requests, this is a singleton
suggestions = Suggestions.instance()

# start the now playing listener and speaker communication
speaker = speaker_communication.Speaker("localhost:8001")


def signal_handler(sig, frame):
    global speaker
    print("Shutting down...")
    util.perform_atomic_operation(speaker.running_lock, speaker.set_is_running, False)
    speaker.thread.join()
    sys.exit(0)


if __name__ == "__main__":
    # set up a signal handler for if a user hits ctrl + c
    signal.signal(signal.SIGINT, signal_handler)
    # start the flask server to handle incoming requests
    server.app.run()
