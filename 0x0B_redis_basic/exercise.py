#!/usr/bin/env python3
"""Redis cache basics module"""


import redis
import uuid

from typing import Tuple


class Cache:
    """ Cache class
        description: stores cache data using redis
    """
    def __init__(self):
        """ Class constructor
        """
        self._redis = redis.Redis()

    def store(self, data: Tuple[str, bytes, int, float]) -> str:
        """
        store - method that stores data in a redis instance
        Args:
            - data: data to store in redis
        Return:
            - string
        """
        random_key = str(uuid.uuid4())
        self._redis.mset({random_key: data})
        return random_value
