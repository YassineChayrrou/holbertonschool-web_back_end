#!/usr/bin/env python3
"""type-annotated function safely_get_value 2"""


from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safety_get_value: use safely_get_value.__annotations__ for types"""
    if key in dct:
        return dct[key]
    else:
        return default
