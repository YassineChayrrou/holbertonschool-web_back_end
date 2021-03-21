#!/usr/bin/python3
"""LRU cache model"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching"""

    LRU_Dictionary = {}

    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Assigns item value to key in self.cache_data
           Deletes Least Recently Used element in self.cache_data if number of
           items self.cache_data is higher then BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if LRUCache.LRU_Dictionary:
                print(LRUCache.LRU_Dictionary)
                my_key = None
                my_value = list(LRUCache.LRU_Dictionary.values())[0]
                for lru_key in LRUCache.LRU_Dictionary:
                    if my_value >= LRUCache.LRU_Dictionary[lru_key]:
                        my_key = lru_key
                        my_value = LRUCache.LRU_Dictionary[lru_key]
                self.cache_data.pop(my_key)
                LRUCache.LRU_Dictionary.pop(my_key)
                print(f"Discard: {my_key}")

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        if key not in LRUCache.LRU_Dictionary.keys():
            LRUCache.LRU_Dictionary[key] = 1
        else:
            LRUCache.LRU_Dictionary[key] += 1
        return self.cache_data[key]
