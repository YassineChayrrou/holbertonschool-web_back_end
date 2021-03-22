#!/usr/bin/python3
"""LFU caching model"""


BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LIFOCache inherits from BaseCaching"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.lfu_cache = {}

    def put(self, key, item):
        """Assigns item value to key in self.cache_data
           Deletes element in self.cache_data using FLU algorithm if item count
           is bigger then MAX_ITEMS
        """
        if key is None or item is None:
            return
        if key not in self.lfu_cache:
            self.lfu_cache[key] = 0
        self.cache_data[key] = item
        lfu_backup = self.lfu_cache.popitem()
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_key = min(self.lfu_cache, key=lambda k: self.lfu_cache[k])
            self.lfu_cache.pop(lfu_key)
            self.cache_data.pop(lfu_key)
            print(f"DISCARD: {lfu_key}")
        self.lfu_cache[lfu_backup[0]] = lfu_backup[1]

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.lfu_cache[key] += 1
        return self.cache_data[key]
