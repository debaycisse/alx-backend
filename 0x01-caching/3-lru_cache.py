#!/usr/bin/env python3
"""This module houses the definition of a class, named LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This implements a cache, using the LRU (Least Recently Used)
    algorithm for the cache replacement policy"""

    def __init__(self):
        """Initializes an instance of this class"""
        super().__init__()
        self.lru_queue = []

    def get_LRU(self):
        """
        Obtains the least frequently used data from the cache

        Args:
            the key of the first item that has a least recently used value
        """
        lru = None

        for d in self.data_frequencies:
            if self.data_frequencies[d] <= 0:
                lru = d
                break
        if not lru:
            for dt in self.data_frequencies:
                if self.data_frequencies[dt] - 1 == 0:
                    lru = dt
                    break
        return lru

    def put(self, key, item):
        """Puts data inside the cache storage

        Args:
            key - this is mapped with a given item and stored in the cache
            item - the value to mapped with a given key in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key in self.cache_data:
                if key in self.lru_queue:
                    self.lru_queue.remove(key)
            else:
                lru_key = self.lru_queue[-1]
                self.cache_data.pop(lru_key)
                print('DISCARD: {0}'.format(lru_key))
                self.lru_queue.remove(lru_key)
        self.lru_queue.insert(0, key)
        self.cache_data.update({key: item})

    def get(self, key):
        """Retrieves data whose key is given from the cache

        Args:
            key - a key with which an item is searched for in the cache

        Returns:
            the item is returned if found, otherwise None is returned
        """
        data = self.cache_data.get(key)
        if data:
            if key in self.lru_queue:
                self.lru_queue.remove(key)
            self.lru_queue.insert(0, key)
        return data
