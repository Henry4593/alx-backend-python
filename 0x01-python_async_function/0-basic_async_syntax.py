#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronous function that waits for a random delay between 0 and
    max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time.
    """
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
