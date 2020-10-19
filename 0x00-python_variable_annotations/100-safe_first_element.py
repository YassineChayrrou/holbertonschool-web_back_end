#!/usr/bin/env python3
"""duck-typed annotations"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element: takes Sequence of any type, returns first element"""
    if lst:
        return lst[0]
    else:
        return None
