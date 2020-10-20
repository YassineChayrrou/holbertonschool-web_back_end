#!/usr/bin/env python3
"""python async basics task 1"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n: spawn wait_random n times with delay equals to max_delay"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    record = []
    for task in asyncio.as_completed(tasks):
        delay: float = await task
        record.append(delay)
    return record
