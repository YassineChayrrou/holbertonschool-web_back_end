#!/usr/bin/env python3
"""type annotated function sum_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list: takes list of floats and return their sum as float"""
    list_sum: float = 0
    for i in input_list:
        list_sum += i
    return list_sum
