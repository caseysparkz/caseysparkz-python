#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Date: April 11, 2023
# Description:
'''The description of the script goes here.'''

__author__ = 'Casey Sparks'

from locale import setlocale, LC_ALL
from logging import getLogger
from typing import Any, Union
from .checks.schema_validation import ValidateSchema

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.

LOG = getLogger(__name__)                                                   # Instantiate logger.


def binary_search(
    sorted_list: list,
    item: Any
        ) -> Union[int, None]:
    '''
    Iteratively search a sorted array for an item and return its index.
    Space complexity of O(1).
        :param sorted_list: The sorted list to search through.
        :param item:        The object in the list to search for.
        :return:            The index of the item, if it exists, or None.
    '''
    test_list = sorted_list                                                 # For parameter validation.
    test_list.sort()

    assert isinstance(sorted_list, list), 'Item must be a list.'
    assert sorted_list == test_list, 'List must be sorted.'
    assert ValidateSchema.max_iterable_depth(sorted_list) == 1, 'List must not have depth > 1.'

    low = 0
    high = len(sorted_list) - 1

    while low <= high:                                                      # Base case.
        mid = (high + low) // 2

        if sorted_list[mid] < item:                                         # Search right sub-array.
            low = mid + 1

        elif sorted_list[mid] > item:                                       # Search left sub-array.
            high = mid - 1

        else:                                                               # Element at middle.
            return mid

    return None                                                             # Element not present.
