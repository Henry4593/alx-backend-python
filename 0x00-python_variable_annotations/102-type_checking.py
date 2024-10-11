#!/usr/bin/env python3
"""
This script contains a function to zoom into an array by repeating itselements.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into an array by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int): The number of times to repeat each element. Default is 2.

    Returns:
        List[int]: A list with each element of the input tuple repeated.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
