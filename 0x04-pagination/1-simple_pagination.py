#!/usr/bin/env python3
"""Simple pagination module
"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Function that returns start & end index of pagination parameters
    """
    end = page * page_size
    start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets page dataset
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        tup = index_range(page, page_size)
        pagination_dataset = []
        try:
            for i in range(tup[0], tup[1]):
                pagination_dataset.append(self.dataset()[i])
        except IndexError:
            return []
        return pagination_dataset
