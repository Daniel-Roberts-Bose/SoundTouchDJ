"""
util.py
Contains utility functions for use in the application
@author Daniel Roberts
"""
import json
import random
import xml.etree.ElementTree as ET


# helper function for creating json information
def make_json(**kwargs):
    return json.dumps(dict(kwargs.items()))


def make_random_request_id():
    return random.getrandbits(128)


def perform_atomic_operation(lock, func, *argv):
    """
    Perform a thread safe operation on the given function
    :param lock: the mutex the lock
    :param func: the function object to call
    :param argv: the arguments, if any, to pass to the function
    """
    lock.acquire()
    func(*argv)
    lock.release()


def perform_atomic_get(lock, func, *argv):
    """
    Perform a thread safe get on a given function
    :param lock: the mutex the lock
    :param func: the function object to call
    :param argv: the arguments, if any, to pass to the function
    :return:
    """
    lock.acquire()
    var = func(*argv)
    lock.release()
    return var


# generic helper function to help parse the now playing xml into a python object
def parse_now_playing(resp):
    # parse the xml formatted response
    tree = ET.parse(resp.content)
    root = tree.getroot()
    if root.tag != 'nowPlaying':
        # some error occurred in speaker communication, increment error count
        print("Could not get nowPlaying information")
        print(resp.content)
        return None
    else:
        return tree


# returns the play status object from within a now playing response, if possible
def get_now_playing_play_status(resp):
    tree = parse_now_playing(resp)
    if tree is None:
        return None

    return tree.findall('playStatus')
