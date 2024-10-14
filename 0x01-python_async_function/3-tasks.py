#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio Task.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio Task that will wait for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
