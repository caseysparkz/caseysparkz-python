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
'''Functions to manipulate lists.'''


from csv import DictWriter
from io import StringIO
from locale import setlocale, LC_ALL
from logging import getLogger
from .Schema import Validate


log = getLogger(__name__)                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                            # Set locale.


def to_csv(
    data: list
        ) -> str:
    '''
    Converts a list of dicts to CSV format.
    Dicts must all have the same keys in order for this function to pull the CSV headers.
        :param data:    A list of dicts to parse into CSV.
    '''
    if not Validate.list_of_dicts(data, common_keys=True):
        raise ValueError('The parameter passed needs to be a list of dicts with common keys.')

    string_fh = StringIO()
    writer = DictWriter(string_fh, data[0].keys())

    writer.writeheader()
    writer.writerows(data)

    return string_fh.getvalue()
