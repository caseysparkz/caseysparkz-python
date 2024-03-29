#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''List manipulation.'''

from csv import DictWriter
from io import StringIO
from locale import setlocale, LC_ALL
from logging import getLogger
from schema import SchemaError
from ..checks.schema_validation import ValidateSchema


log = getLogger(__name__)                                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.utf-8')                                            # Set locale.


def to_csv(
    data: list
        ) -> str:
    '''
    Converts a list of dicts to CSV format.
    Dicts must all have the same keys in order for this function to pull the CSV headers.
        :param data:    A list of dicts to parse into CSV.
        :return:        A string containing the CSV data.
    '''
    if not ValidateSchema.list_of_dicts(data, common_keys=True):
        raise SchemaError('The parameter passed needs to be a list of dicts with common keys.')

    string_fh = StringIO()
    writer = DictWriter(string_fh, data[0].keys())

    writer.writeheader()
    writer.writerows(data)

    return string_fh.getvalue()
