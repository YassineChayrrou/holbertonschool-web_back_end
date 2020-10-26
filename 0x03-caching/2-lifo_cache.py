#!/usr/bin/python3
"""LIFO caching model"""


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching"""

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assigns item value to key in self.cache_data
           Deletes first element in self.cache_data if elements count is bigger
           then MAX_ITEMS
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = sorted(self.cache_data).pop()
                self.cache_data[key] = item
                print("DISCARD: {}".format(last))
            else:
                self.cache_data[key] = item

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
