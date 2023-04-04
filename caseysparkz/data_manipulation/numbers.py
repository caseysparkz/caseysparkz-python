#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Integer/float manipulation.'''

from logging import getLogger
from locale import setlocale, LC_ALL
from typing import Union

log = getLogger(__name__)                                                   # Enable logging.

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.


def to_sig_fig_float(
    number: Union[int, float],
    significant_figures: int
        ) -> float:
    '''
    Convert a float or int to a float with significant figures specified by user.
        :param number:              The float/integer to round.
        :param significant_figures: The number of significant figures to round to.
        :return:                    Float containing specified sig-figs.
    '''
    return float(f'{number:.{significant_figures}g}')


def seconds_to_short_time(
    secs: int
        ) -> str:
    '''
    Converts seconds to XdYhZm format.
        :param secs:    The 'seconds' integer to convert to a string.
        :return:        Time string.
    '''
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)

    retval = ''.join([
        f'{value}{key}'
        for key, value
        in {'d': days,  'h': hours, 'm': mins, 's': secs}.items()
        if value != 0
    ])

    return retval
