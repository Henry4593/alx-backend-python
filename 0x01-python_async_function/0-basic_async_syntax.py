#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.
"""

import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """
    Asynchronous function that waits for a random delay between 0 and
    max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time.
    """
    max_delay = uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return max_delay
