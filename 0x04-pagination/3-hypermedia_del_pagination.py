#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns dict formatted according to HATEOS"""
        assert type(index) is int
        assert type(page_size) is int
        assert index >= 0
        assert index <= len(self.dataset())
        next_index = index
        hypermedia_data = []
        for i in range(page_size):
            try:
                hypermedia_data.append(self.indexed_dataset()[next_index])
                # print(f"next_index : {next_index} is valid")
            except KeyError:
                # print(f"next_index : {next_index} is not valid")
                next_index += 1
            next_index += 1
        # print("loop ends here!!!!")
        return {
            'index': index,
            'data': hypermedia_data,
            'next_index': next_index,
            'page_size': page_size
        }
