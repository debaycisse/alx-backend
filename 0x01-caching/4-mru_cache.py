#!/usr/bin/env python3
"""This module houses the implementation of a class, named MRUCaching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This class implements a cache system, using MRU
    (Most recently used) for the cache replacement policy"""

    def __init__(self):
        """This method initializes an instance of this class"""
        super().__init__()
        self.mru_queue = []

    def put(self, key, item):
        """Stores a given key and value in the cache, using MRU"""
        if key is None or item is None:
            return
        if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
            if key not in self.mru_queue:
                _key = self.mru_queue[0]
                self.cache_data.pop(_key)
                print('DISCARD: {0}'.format(_key))
                self.mru_queue.pop(0)
            else:
                self.mru_queue.remove(key)

        self.mru_queue.insert(0, key)
        self.cache_data.update({key: item})

    def get(self, key):
        """
        Retrieves the value of a given key from the cache

        Args:
            key - key to be used to retrieve the value from the cache

        Returns:
            the found value or none if no value is found
        """
        item = self.cache_data.get(key)
        if item is not None:
            if key in self.mru_queue:
                self.mru_queue.remove(key)
                self.mru_queue.insert(0, key)
        return item
