#!/usr/bin/env python3
"""
This module contains a function that runs multiple coroutines concurrently
and returns their results in a sorted list.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times with the specified max_delay and return the list
    of delays in ascending order.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    wait_time = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_time)
