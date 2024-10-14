#!/usr/bin/env python3
"""
Module to measure the runtime of an asynchronous function.
"""
import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of the wait_n function.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call.

    Returns:
        float: The average runtime per call.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    return (time() - start_time) / n
