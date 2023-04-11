#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Date: April 11, 2023
# Description:
'''The description of the script goes here.'''

__author__ = 'Casey Sparks'

from locale import setlocale, LC_ALL
from logging import getLogger
from typing import Any, Optional, Union

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.

LOG = getLogger(__name__)                                                   # Instantiate logger.


def binary_search_iterative(
    sorted_list: list,
    item: Any
        ) -> Union[int, None]:
    '''
    Iteratively search a sorted array for an item and return its index.
        :param sorted_list: The sorted list to search through.
        :param item:        The object in the list to search for.
    '''
    assert isinstance(sorted_list, list), 'Item must be a list.'
    assert sorted_list.sort() == sorted_list, 'List must be sorted.'

    low = 0
    high = len(arr) - 1

    while low <= high:                                                      # Base case.
        mid = (high + low) // 2

        if arr[mid] < x:                                                    # Search right sub-array.
            low = mid + 1

        elif arr[mid] > x:                                                  # Search left sub-array.
            high = mid - 1

        else:                                                               # Element at middle.
            return mid

    return None                                                             # Element not present.


def binary_search_recursive(
    sorted_list: list,
    item: Any,
    low: Optional[int] = None,
    high: Optional[int] = None,
        ):
    '''
    Recursively search a sorted array for an item and return its index.
        :param sorted_list: The sorted list to search through.
        :param item:        The object in the list to search for.
        :param low:         The lowest index in a given sub-array.
        :param high:        The highest index in a given sub-array.
    '''
    assert isinstance(sorted_list, list), 'Item must be a list.'
    assert sorted_list.sort() == sorted_list, 'List must be sorted.'

    if not low:
        low = 0

    if not high:
        high = len(sorted_list) -1

    if high >= low:                                                         # Base case.
        mid = (high + low) // 2

        if sorted_list[mid] == item:                                        # Element at middle.
            return mid

        if sorted_list[mid] > item:                                         # Search left sub-array.
            return binary_search_recursive(sorted_list, item, low, mid - 1)

        return binary_search_recursive(sorted_list, item, mid + 1, high)    # Search right sub-array.

    return None                                                             # Not present.
