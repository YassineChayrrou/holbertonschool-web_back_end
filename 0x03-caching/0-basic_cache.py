#!/usr/bin/python3
"""BasicCache module"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching"""
    def put(self, key, item):
        """Assigns item value to key in self.cache_data"""
        if key and item:
            self.cache_data[key] = item
        pass

    def get(self, key):
        """returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
