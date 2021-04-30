#!/usr/bin/env python3
""" Web Cache and Tracker module """


import redis
import requests
from time import sleep
from typing import Callable
from functools import wraps


_redis = redis.Redis()


def url_cache(fn: Callable) -> Callable:
    """
    url_cache - counts requests of a url and cache the response on redis
                instance.
    Args:
        - fn: Callable, function to pass and count how many times its invoked
    Return:
        - returns HTML from cache is cache is not expired
    """
    @wraps(fn)
    def wrapper(url):
        key = "count:{}".format(url)
        cache = "cache:{}".format(url)
        response = _redis.get(cache)

        _redis.incr(key, 1)
        if response:
            print("returned from cache")
            return response
        output = fn(url)
        _redis.setex(cache, 10, output)
        print("returned through api")
        return fn(url)
    return wrapper


@url_cache
def get_page(url: str) -> str:
    """
    get_page - gets html of requested url
    """
    page = requests.get(url).text
    return page
