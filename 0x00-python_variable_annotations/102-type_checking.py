#!/usr/bin/env python3
"""zoom_array"""


from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zoom_array: takes tuple and int, returns list of tuple elements multipl-
    ited by factor
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
