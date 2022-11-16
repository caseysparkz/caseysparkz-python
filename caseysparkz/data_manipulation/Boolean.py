#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Functions to manipulate bools.'''


from locale import setlocale, LC_ALL
from logging import getLogger
from typing import Iterable


log = getLogger(__name__)                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                            # Set locale.


def none(
    boolean_iterable: Iterable
        ) -> bool:
    '''
    The opposite of the any() built-in; returns True if the iterable contains no True elements.
        :param boolean_iterable:    An iterable containing elements to be assessed as booleans.
    '''
    return not any(boolean_iterable)
