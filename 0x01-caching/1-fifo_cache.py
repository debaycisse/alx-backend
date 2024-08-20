#!/usr/bin/env python3
"""This module houses a definition of a class, named FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class implements a caching algorithm, using the FIFO"""

    def __init__(self):
        """Initializes an instance of this class"""
        super().__init__()

    def put(self, key, item):
        """
        Inserts a given key and value into the cache store

        Args:
            key - key to map to the new item in the cache
            item - an item with which a given key is mapped
        """
        if (key is not None) and (item is not None):
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
               self.cache_data.get(key) is None):
                keys = [k for k in self.cache_data.keys()]
                self.cache_data.pop(keys[0])
                print('DISCARD: {0}'.format(keys[0]))
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
