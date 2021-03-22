#!/usr/bin/python3
"""MRU caching model"""


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """LIFOCache inherits from BaseCaching"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.mru_cache = []

    def put(self, key, item):
        """Assigns item value to key in self.cache_data
           Deletes element in self.cache_data using MRU algorithm if item count
           is bigger then MAX_ITEMS
        """
        if key is None or item is None:
            return
        if key not in self.mru_cache:
            self.mru_cache.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_cache.pop(len(self.mru_cache) - 2)
            self.cache_data.pop(mru_key)
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        recent_used_key = self.mru_cache.pop(self.mru_cache.index(key))
        self.mru_cache.append(recent_used_key)
        return self.cache_data[key]
