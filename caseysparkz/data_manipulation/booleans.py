#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Boolean manipulation.'''

from locale import setlocale, LC_ALL
from logging import getLogger
from typing import Iterable


log = getLogger(__name__)                                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.utf-8')                                            # Set locale.


def none(
    boolean_iterable: Iterable
        ) -> bool:
    '''
    The opposite of the any() built-in; returns True if the iterable contains no True elements.
        :param boolean_iterable:    An iterable containing elements to be assessed as booleans.
        :return:                    Returns True if non in iterable are True else False.
    '''
    bools_in_list = [isinstance(item, bool) for item in boolean_iterable]

    assert isinstance(boolean_iterable, Iterable), '`boolean_iterable` must be an iterable.'
    assert all(bools_in_list), '`boolean_iterable` contain only bools.'

    return not any(boolean_iterable)
