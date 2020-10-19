#!/usr/bin/env python3
"""type annotated function element_length"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length: takes iterable sequence, returns a list of tuples """
    return [(i, len(i)) for i in lst]
