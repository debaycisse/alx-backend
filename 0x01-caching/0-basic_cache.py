#!/usr/bin/env python3
"""This module houses a definition of a class, named BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class inherits from the BaseCaching to
    implement cache system with no limit"""

    def __init__(self):
        """This method initializes an instance of this class"""
        super().__init__()

    def put(self, key, item):
        """
        Stores or puts the given key and value in the cache data

        Args:
            key - the key to the new data to be cached
            value - value to be mapped with the key
        """
        if (key is not None) and (item is not None):
            self.cache_data[str(key)] = item

    def get(self, key):
        """
        Retrieves value, linked mapped to a given key from the cache

        Args:
            key - key with which a value is mapped

        Returns:
            a found value, or None if no data is found
        """
        return self.cache_data.get(key)
