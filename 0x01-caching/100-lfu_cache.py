#!/usr/bin/env python3
"""This module houses the definition of a class, named LFUCache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements cache system, using LRU (Least Recently Used)
    cache replacement algorithm"""

    def __init__(self):
        """Initializes an instance of this class"""
        super().__init__()
        # contains each key, maximum of 4
        self._keys = []
        # contains instances of keys, updates as keys are used
        self.counts = []

    """def get_highest_FU(self):
        hfu = 0
        for key in self.counts:
            if self.counts.count(key) > hfu:
                hfu = self.counts.count(key)
        return hfu"""

    def get_lfu(self):
        """Obtains LFU (Least Frequency Used) key

        Returns:
            the first key with the least frequency used value
        """
        rm_key = None
        fr = 1
        while rm_key is None:
            k = -1
            for n in range(4):
                if self.counts.count(self._keys[k]) <= fr:
                    rm_key = self._keys[k]
                    break
                k -= 1
            fr += 1
        return rm_key

    def remove_keys(self, k):
        """Removes all instance of a key

        Args:
            k - a given whose instances are completely removed from a list
        """
        for key in self.counts:
            if key == k:
                self.counts.remove(key)

    def put(self, key, item):
        """Places a given key and item in the cache

        Args:
            key - the key to be mapped with a typical item
            item - the actual item or value to map the key with
        """
        if key is None or item is None:
            return
        if (key not in self.cache_data):
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lfu = self.get_lfu()
                self.cache_data.pop(lfu)
                print('DISCARD: {0}'.format(lfu))
                self._keys.remove(lfu)
                self.remove_keys(lfu)
                self._keys.insert(0, key)
                self.counts.append(key)
                self.cache_data.update({key: item})
            else:
                self.cache_data.update({key: item})
                self._keys.insert(0, key)
                self.counts.append(key)
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                self.cache_data.update({key: item})
                if key in self._keys:
                    self._keys.remove(key)
                self._keys.insert(0, key)
                self.counts.append(key)

            else:
                self.cache_data.update({key: item})
                self._keys.insert(0, key)
                self.counts.append(key)

    def get(self, key):
        """Retrieves a mapped value via a given key

        Args:
            key - key to be used to look up its assigned value or item

        Returns:
            a found value is returned if found, otherwise None is returned
        """
        item = self.cache_data.get(key)
        if item:
            if key in self._keys:
                self._keys.remove(key)
            self._keys.insert(0, key)
            self.counts.append(key)
        return item
