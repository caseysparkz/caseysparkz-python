#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Integer/float manipulation.'''

from logging import getLogger
from locale import setlocale, LC_ALL
from ..exceptions import MutuallyExclusiveArgumentError

LOG = getLogger(__name__)                                                   # Enable logging.

setlocale(LC_ALL, 'en_US.utf-8')                                            # Set locale.


class Integer():
    '''Methods for integer manipulation.'''
    @staticmethod
    def seconds_to_short_time(
        seconds: int,
        exclude_zero_values: bool = False,
        rounded: bool = False
            ) -> str:
        '''
        Converts seconds to XdYh format.
        `exclude_zero_values` and `rounded` are mutually exclusive.
            :param seconds:             Number of seconds.
            :param exclude_zero_values: Include values like '0d' and '0h' in the return string.
            :param rounded:             Round return string to most significant values (like '15d0h1m' -> '15d').
            :return:                    A formatted time string, like '1d59m3s'.
        '''
        assert isinstance(seconds, int), '`seconds` must be int'
        assert isinstance(exclude_zero_values, bool), '`exclude_zero_values` must be bool'
        assert isinstance(rounded, bool), '`rounded` must be bool'

        if exclude_zero_values and rounded:
            raise MutuallyExclusiveArgumentError(['exclude_zero_values', 'rounded'])

        time_d = {'d': 0, 'h': 0, 'm': 0, 's': 0}                           # Maintain unit order.
        time_d['m'], time_d['s'] = divmod(seconds, 60)                      # Get minutes and seconds.
        time_d['h'], time_d['m'] = divmod(time_d['m'], 60)                  # Get hours and minutes.
        time_d['d'], time_d['h'] = divmod(time_d['h'], 24)                  # Get days and hours.

        LOG.debug(f'Time values: {time_d}')

        if exclude_zero_values:                                             # Exclude zero values.
            time_s = ''.join([f'{v}{k}' for (k, v) in time_d.items() if v])

        elif rounded:                                                       # Round to first zero unit.
            time_s = ''

            for key, value in time_d.items():
                if value == 0 and time_s:
                    break

                if value == 0:
                    continue

                time_s += f'{value}{key}'

        else:                                                               # Full time-string data.
            time_s = ''.join([f'{v}{k}' for (k, v) in time_d.items()])

        return time_s
