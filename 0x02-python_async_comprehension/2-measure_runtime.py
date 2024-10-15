#!/usr/bin/env python3
"""
Module to measure the runtime of executing async comprehensions concurrently.
"""
from time import time
import asyncio
from importlib import import_module

async_comprehension = import_module(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times
    concurrently.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start_time
