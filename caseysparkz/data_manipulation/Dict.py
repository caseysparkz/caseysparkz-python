#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''
Dictionary manipulation.
'''

from locale import setlocale, LC_ALL
from logging import getLogger


log = getLogger(__name__)                               # Instantiate parser.

setlocale(LC_ALL, 'en_US.UTF-8')                        # Set locale.


def to_string(
    data: dict,
    kv_separator: str = '=',
    object_separator: str = '\n'
        ) -> str:
    '''
    Converts a dictionary to a single string with user-defined delineators.
        :param data:                The dictionary to format into a string.
        :param kv_separator:        The string separating keys and values.
        :param object_separator:    The string separating key/value pairs.
    '''
    return object_separator.join([f'{key}{kv_separator}{data[key]}' for key in data])
