#!/usr/bin/env python3
"""This module houses the definition of a class,
named Server along with its methods"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    computes a starting and ending indexes of a list, needed to obtain a
    given number of elements, based on the page and page_size

    Args:
        page - the starting index's value,
        taking note that list is zero-based index
        page_size - the number of items to display per page

    Returns:
        a tuple, containing the starting and ending index values
    """
    if not isinstance(page, int):
        raise ValueError('page must be an integer')
    if not isinstance(page_size, int):
        raise ValueError('page size must be an integer')

    st = (page - 1) * page_size
    ed = st + page_size
    return (st, ed)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset by fetching and storing the data from the csv file
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        obtains page size's number of items for the given page's value

        Args:
            page - the starting index's value, minus 1
            page_size - the number of items to be returned

        Returns:
            list of the list of the items, using the computed indices' ranges
        """
        assert type(page) is int
        assert page > 0
        assert type(page_size) is int
        assert page_size > 0
        s_index, e_index = index_range(page, page_size)
        dataset = self.dataset()
        try:
            data = dataset[s_index: e_index]
        except IndexError:
            data = []
        return data
