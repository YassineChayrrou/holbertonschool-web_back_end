#!/usr/bin/env python3
""" Web Cache and Tracker module """


from time import sleep
import redis
import requests
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
    def wrapper(self, *args, **kwargs):
        key = "count:{" + str(self) + "}"
        cache = "cache:{" + str(self) + "}"
        response = _redis.get(cache)

        _redis.incr(key, 1)
        if response:
            return response
        output = fn(self, *args, **kwargs)
        _redis.mset({cache: output})
        _redis.expire(cache, 10)
        return fn(self, *args, **kwargs)
    return wrapper


@url_cache
def get_page(url: str) -> str:
    """
    get_page - gets html of requested url
    """
    page = requests.get(url).text
    return page


if __name__ == "__main__":
    url = 'https://dog.ceo'
    req = get_page(url)
    sleep(3)
    req2 = get_page(url)
    sleep(2)
    req3 = get_page(url)
    sleep(1)
    req4 = get_page(url)
    sleep(6)
    req5 = get_page(url)
