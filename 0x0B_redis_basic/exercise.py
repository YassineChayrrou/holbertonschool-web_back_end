#!/usr/bin/env python3
"""Redis cache basics module"""


import redis
import uuid

from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count_calls - counts how many times a method is called
    Args:
        - method: Callable, method to count how many times is invoked
    Return:
        - wrapper: wrapperfunction for function decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history - Stores history of inputs and outputs of a callabe (method)
    Args:
        - method: Callable, function or method executed
    Return:
        - wrapper: wrapper function for decorator to return
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(inputs, str(args))
        output = str(method(self, *args))
        self._redis.rpush(outputs, output)
        return output
    return wrapper


class Cache:
    """ Cache class
        description: stores cache data using redis
    """
    def __init__(self):
        """ Class constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store - method that stores data in a redis instance
        Args:
            - data: data to store in redis
        Return:
            - random_key: key string
        """
        random_key = str(uuid.uuid4())
        self._redis.mset({random_key: data})
        return random_key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        get - gets data from redis and recovers its original type
        Args:
            - key: str, value of key stored in redis DB
            -fn: callable, converts data to desired format
        Return:
            - value
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        get_str - returns a string value from redis db
        Args:
            - value: str, key searchable in redis
        Return:
            - value: str, string format requested key
        """
        value = self.get(key, str)
        return value

    def get_int(self, key: int) -> int:
        """
        get_int - returns an integer value from redis db
        Args:
            - key: int, key searchable in redis
        Return:
            - value:int, integer foramt of requested key
        """
        value = self.get(key, int)
        return value
