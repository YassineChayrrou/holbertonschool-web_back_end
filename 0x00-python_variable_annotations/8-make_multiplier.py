#!/usr/bin/env python3
"""type-annotated function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier: takes a floatreturns a function that multiplies a float
    """
    return lambda x: x * multiplier
