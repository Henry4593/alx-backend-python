#!/usr/bin/env python3
"""
Module for async comprehension.
"""

from typing import List
from importlib import import_module


async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing over
    async_generator.

    Returns:
        List[float]: A list of 10 random floating point numbers.
    """
    return [float_num async for float_num in async_generator()]
