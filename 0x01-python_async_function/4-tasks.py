#!/usr/bin/env python3
"""
This module contains an asynchronous function that runs multiple tasks
concurrently and returns their results in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run the task_wait_random function n times with the specified max_delay and
    return the list of delays in ascending order.

    Args:
        n (int): The number of times to run task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    wait_time = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_time)
