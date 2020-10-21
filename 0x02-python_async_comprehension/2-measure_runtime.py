#!/usr/bin/env python3
"""python async list comprehension"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure_runtime: mesures total runtime"""
    s = time.perf_counter()
    taskList = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(taskList)
    elapsed = time.perf_counter() - s
    return elapsed
