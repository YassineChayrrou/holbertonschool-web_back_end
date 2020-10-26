#!/usr/bin/python3
"""FIFP caching model"""


BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assigns item value to key in self.cache_data
           Deletes first element in self.cache_data if elements count is bigger
           then MAX_ITEMS
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first = sorted(self.cache_data)
            self.cache_data.pop(first[0])
            print("DISCARD: {}".format(first[0]))

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
