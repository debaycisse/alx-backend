#!/usr/bin/env python3
"""This module houses the definiton of a function, named index_range"""

from typing import Tuple


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
