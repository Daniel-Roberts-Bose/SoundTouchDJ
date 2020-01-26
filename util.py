"""
util.py
Contains utility functions for use in the application
@author Daniel Roberts
"""
import json
import random


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
