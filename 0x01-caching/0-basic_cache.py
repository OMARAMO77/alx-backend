#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that inherits from BaseCaching
    and is a caching system
    """
    def put(self, key, item):
        """Store a key-value pair in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return value linked to key.
        """
        return self.cache_data.get(key, None)
