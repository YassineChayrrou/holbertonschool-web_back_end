#!/usr/bin/env python3
"""python async comprehension"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """async_comprehension: returns a list of numbers passed from async func
       using async list comprehension
    """
    return [i async for i in async_generator()]
