#!/usr/bin/env python3
"""Redis cache basics module"""


import redis
import uuid

from typing import Callable, Union


class Cache:
    """ Cache class
        description: stores cache data using redis
    """
    def __init__(self):
        """ Class constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    def get(self, key: str, fn: Callable):
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
