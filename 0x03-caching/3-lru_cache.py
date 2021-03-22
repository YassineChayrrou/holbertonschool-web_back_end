#!/usr/bin/python3
"""LRU cache model"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.lru_cache = []

    def put(self, key, item):
        """Assigns item value to key in self.cache_data
           Deletes Least Recently Used element in self.cache_data if number of
           items self.cache_data is higher then BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        if key not in self.lru_cache:
            self.lru_cache.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            my_key = self.lru_cache.pop(0)
            self.cache_data.pop(my_key)

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.lru_cache:
            recent_key = self.lru_cache.pop(self.lru_cache.index(key))
            self.lru_cache.append(recent_key)
        return self.cache_data[key]
