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
'''Integer/float manipulation.'''


import logging
import locale
from typing import Union

log = logging.getLogger(__name__)                                   # Enable logging.
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')                      # Set locale.


def to_sig_fig_float(
    number: Union[int, float],
    significant_figures: int
        ) -> float:
    '''
    Convert a float or int to a float with significant figures specified by user.
        :param number:              The float/integer to round.
        :param significant_figures: The number of significant figures to round to.
    '''
    return float('%s' % f'%.{significant_figures}g' % number)


def seconds_to_short_time(
    secs: int
        ) -> str:
    '''
    Converts seconds to XdYh format.
        :param secs: The 'seconds' integer to convert to a string.
    '''
    # Nested if statements keep it from being too long by lopping off non-significant values.
    retval = str()

    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)

    if days:
        retval += f'{days}d'

    if hours:
        retval += f'{hours}h'

        if days > 0:
            return retval

    if mins:
        retval += f'{mins}m'

        if hours or days:
            return retval

    if secs:
        retval += f'{secs}s'

    return retval
