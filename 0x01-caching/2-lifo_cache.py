#!/usr/bin/env python3
"""This module houses the definition of a class, named LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines:
       cache system, using the LIFO for the cach replacement policy
    """

    def __init__(self):
        """Initializes an instance of this class"""
        super().__init__()

    def put(self, key, item):
        """Inserts or puts in a given key and item in the cache

        Args:
            key - key to be mapped with a given item
            item - item to be mapped with a given key in the cache
        """
        if (key is not None) and (item is not None):
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
               self.cache_data.get(key) is None):
                res = self.cache_data.popitem()
                print('DISCARD: {0}'.format(res[0]))
            elif (self.cache_data.get(key) is not None):
                self.cache_data.pop(key)
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Retrieve the value, found to be mapped with a given key

        Args:
            key - key that is mapped to the value to be retrieved

        Returns:
            the value, mapped with the key or None, if key does not exist
        """
        return self.cache_data.get(key)
