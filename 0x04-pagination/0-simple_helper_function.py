#!/usr/bin/env python3
"""index_range module"""


def index_range(page: int, page_size: int) -> tuple:
    """Function that returns start & end index of pagination parameters
    """
    end = page * page_size
    start = end - page_size
    return (start, end)
