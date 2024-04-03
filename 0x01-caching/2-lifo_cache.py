#!/usr/bin/env python3
"""LIFO caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching
    system with a LIFO removal mechanism
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """Return value linked to key.
        """
        return self.cache_data.get(key, None)
