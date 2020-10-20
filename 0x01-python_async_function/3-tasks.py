#!/usr/bin/env python3
"""python async basics task 1"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random: returns asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
