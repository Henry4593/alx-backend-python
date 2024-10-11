#!/usr/bin/env python3
"""module that defines to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and a value v (either int or float) and returns a
    tuple with k and the square of v as a float
    """
    return (k, (v ** 2))
