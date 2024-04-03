#!/usr/bin/env python3
"""FIFO caching module.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching
    system with a FIFO removal mechanism
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store a key-value pair in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Return value linked to key.
        """
        return self.cache_data.get(key, None)
