#!/usr/bin/env python3
"""LFU caching module.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """inherits from BaseCaching and is a caching
    system with a LFU removal mechanism
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.frequency = {}
        self.min_freq = 0

    def put(self, key, item):
        """Store a key-value pair in the cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequency used item (LFU)
            min_freq_keys = [key for key, freq in self.frequency.items() if freq == self.min_freq]
            if len(min_freq_keys) > 1:
                lru_key = min(min_freq_keys, key=lambda k: self.cache_data[k])
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
            else:
                print("DISCARD:", min_freq_keys[0])
                del self.cache_data[min_freq_keys[0]]
                del self.frequency[min_freq_keys[0]]

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.min_freq = min(self.frequency.values())

    def get(self, key):
        """Return value linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.min_freq = min(self.frequency.values())
        return self.cache_data[key]
