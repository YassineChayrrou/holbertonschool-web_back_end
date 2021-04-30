#!/usr/bin/env python3
""" Web Cache and Tracker module """


import redis
import requests
from typing import Callable
from functools import wraps


reds = redis.Redis()


def count_url_reqs(fn: Callable) -> Callable:
    """
    url_cache - counts requests of a url and cache the response on redis
                instance.
    Args:
        - fn: Callable, function to pass and count how many times its invoked
    Return:
        - returns HTML from cache if not expired
    """
    @wraps(fn)
    def wrapper(url):
        key = "count:{}".format(url)
        cache = "cache:{}".format(url)
        response = reds.get(cache)

        if response:
            return response
        reds.incr(key, 1)
        output = fn(url)
        reds.setex(cache, 10, output)
        return fn(url)
    return wrapper


@count_url_reqs
def get_page(url: str) -> str:
    """
    get_page - gets html of requested url
    Args:
        - url: str, website url
    Return:
        - html content of response
    """
    page = requests.get(url)
    return page.text
