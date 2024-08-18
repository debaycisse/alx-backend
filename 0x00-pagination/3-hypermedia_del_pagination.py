#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


def get_next_index(ds: Dict[int, List], index: int, page_size: int) -> int:
    """
    Obtains the next index value, based on a given index and page size

    Args:
        ds - a dictionary that contains the indexed version of the dataset
        index - value of the index of the first item on the page
        page_size - value of the number of elements per page

    Returns:
        the value for the next index to display on the next page
    """
    total_elements = len(ds)
    next_index = index + page_size
    no_rec = 0
    st_index = index
    if next_index < total_elements:
        for _ in range(page_size):
            if ds.get(st_index) is None:
                no_rec += 1
            st_index += 1
        return no_rec + next_index
    return 0


def get_page_size(ds: Dict[int, List], index: int, pg_size: int) -> int:
    """
    Obtains the value for the next page

    Args:
        ds - a dictionary that contains the indexed version of the dataset
        index - the index of the first element on the page
        pg_size - the number of elements per page
    """
    total_elements = len(ds)
    next_index = index + pg_size
    if next_index < total_elements:
        return pg_size
    return 0


def get_index_data(ds: Dict[int, List], index: int, pg_size: int) -> List:
    """
    Retrieves the element from the indexed version of the dataset

    Args:
        ds - a dictionary that contains the indexed version of the dataset
        index - the index of the first element on the page
        pg_size - the number of elements per page
    """
    st_index = index
    data = []
    for _ in range(pg_size):
        while ds.get(st_index) is None:
            st_index += 1
        data.append(ds.get(st_index))
        st_index += 1
    return data


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Union[int, None] = None,
                        page_size: int = 10) -> Dict:
        """
        Obtains hyper information of a given index

        Args:
            index - the index of the first element on the returned page
            page_size - the number of element to be present on a page
        """
        self.indexed_dataset()
        assert type(index) is int
        assert index < len(self.__indexed_dataset)
        assert type(page_size) is int
        next_index = get_next_index(self.__indexed_dataset, index, page_size)
        page_s = get_page_size(self.__indexed_dataset, index, page_size)
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_s,
            'data': get_index_data(self.__indexed_dataset, index, page_size)
        }
