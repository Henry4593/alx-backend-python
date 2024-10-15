#!/usr/bin/env python3
"""This module contains an asynchronous generator function."""

import asyncio
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10.
    The generator will sleep for 1 second between each yield.
    It will yield a total of 10 random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random() * 10
