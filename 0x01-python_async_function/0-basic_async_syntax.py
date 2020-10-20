#!/usr/bin/env python3
"""asyncronous coroutine"""

import asyncio
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random: takes int max_delay, waits for random delay and returns it
    """
    random_delay = random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
