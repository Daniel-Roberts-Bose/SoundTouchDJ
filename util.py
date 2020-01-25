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
