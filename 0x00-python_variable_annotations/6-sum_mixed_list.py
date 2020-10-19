#!/usr/bin/env python3
"""type annotated function sum_mixed_list"""


from typing import Union


def sum_mixed_list(mxd_lst: Union[float, int]) -> float:
    """sum_mixed_list: takes list of (int, float) types, returns sum as float
    """
    res = 0
    for i in mxd_lst:
        res += i
    return res
