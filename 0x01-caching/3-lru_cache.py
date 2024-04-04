#!/usr/bin/env python3
"""LRU  caching module.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching
    system with a LRU removal mechanism
    """
    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """Store a key-value pair in the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.key_order.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """Return value linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.key_order.remove(key)
        self.key_order.append(key)
        return self.cache_data[key]
