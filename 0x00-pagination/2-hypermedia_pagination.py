#!/usr/bin/env python3
"""This module houses the definition of a class,
named Server along with its methods"""

import csv
import math
from typing import List, Tuple, Union, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Computes a starting and ending indexes of a list, needed to obtain a
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


def get_prev_page(page: int) -> Union[int, None]:
    """
    Computes the value for the previous page

    Args:
        page - the current page's value

    Returns:
        returns the value if the current page
        is not the first page, otherwise None
    """
    if page - 1 <= 0:
        return None
    return page - 1


def get_next_page(ds: List[List], page: int, p_size: int) -> Union[int, None]:
    """
    Obtains the value for the next page

    Args:
        ds - the dataset which contains all the elements
        page - the current page's value

    Returns:
        if there are more pages to show return the next page, otherwise None
    """
    total_dataset = len(ds)
    item_position = ((page - 1) * p_size) + p_size
    if item_position < total_dataset:
        return page + 1
    return None


def get_total_page(ds: List[List], page_size: int) -> int:
    """
    Obtains the total number of pages, based on a given page's size

    Args:
        ds - the dataset that contains all the elements
        page_size - the value for the number of elements per page

    Returns:
        the total number of pages based on a given page's size
    """
    return math.ceil(len(ds) / page_size)


def get_page_size(ds: List[List], pg: int, pg_sz: int) -> int:
    """
    Obtains the page size's value

    Args:
        ds - the dataset that contains all the elements
        pg - the value of the current page
        pg_sz - the value of the number of elements per page
    """
    total_elements = len(ds)
    element_position = (pg - 1) * pg_sz
    if element_position > total_elements:
        return 0
    return pg_sz


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
        Obtains page size's number of items for the given page's value

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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, object]:
        """
        Obtains hypermedia data for the dataset
        which is stored in self.__dataset

        Args:
            page - the starting index's value, minus 1
            page_size - the number of items to be returned

        Returns:
            list of the list of the items, using the computed indices' ranges
        """
        return {
            'page_size': get_page_size(self.dataset(), page, page_size),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': get_next_page(self.dataset(), page, page_size),
            'prev_page': get_prev_page(page),
            'total_pages': get_total_page(self.dataset(), page_size)
        }
