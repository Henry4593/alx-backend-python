#!/usr/bin/env python3
"""Module that defines a function to create a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its input by the given multiplier"""
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
