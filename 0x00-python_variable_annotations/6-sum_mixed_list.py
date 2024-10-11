#!/usr/bin/env python3
"""Module that defines a function to sum a list of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats and returns their sum as a float"""
    return sum(mxd_lst)
