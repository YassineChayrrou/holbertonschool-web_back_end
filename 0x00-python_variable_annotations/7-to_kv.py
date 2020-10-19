#!/usr/bin/env python3
"""type annotated function to_kv"""


from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv: takes string and (int or float) returns Tuple(str, float)
            v is squared and returned as element of tuple
    """
    squared: float = v**2
    return (k, squared)
