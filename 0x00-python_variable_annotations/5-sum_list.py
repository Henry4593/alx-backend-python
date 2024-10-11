#!/usr/bin/env python3
"""Module that defines a function to sum a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum"""
    sum: float = 0
    for num_float in input_list:
        sum += num_float
    return sum
