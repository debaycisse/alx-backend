#!/usr/bin/env python3
"""This module houses the definition of a class, named LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This implements a cache, using the LRU (Least Recently Used)
    algorithm for the cache replacement policy"""

    def __init__(self):
        """Initializes an instance of this class"""
        super().__init__()
        self.data_frequencies = {}

    def get_LRU(self):
        """
        Obtains the least frequently used data from the cache
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
        if (key is not None) and (item is not None):
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
               self.cache_data.get(key) is None):
                lru = self.get_LRU()
                self.cache_data.pop(lru)
                self.data_frequencies.pop(lru)

                for df in self.data_frequencies:
                    self.data_frequencies[df] -= 1

                print('DISCARD: {0}'.format(lru))

            elif (self.cache_data.get(key) is not None):
                self.data_frequencies.pop(key)
                self.cache_data.pop(key)
            self.cache_data.update({key: item})
            self.data_frequencies.update({key: 1})

    def get(self, key):
        """Retrieves data whose key is given from the cache

        Args:
            key - a key with which an item is searched for in the cache

        Returns:
            the item is returned if found, otherwise None is returned
        """
        data = self.cache_data.get(key)
        if data is not None:
            self.data_frequencies[key] += 1
        return data
