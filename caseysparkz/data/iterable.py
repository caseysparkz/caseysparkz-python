#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         March 06, 2023
# Description:
'''Methods for list processing.'''

from csv import DictWriter
from io import StringIO
from logging import getLogger
from pathlib import Path
from typing import NoReturn
from ..checks.schema_validation import ValidateSchema

LOG = getLogger(__name__)


class List():
    '''Methods for manipulating lists.'''
    @staticmethod
    def to_csv_str(
        data: list,
            ) -> str:
        '''
        Converts a list of dicts to CSV format and returns the string.
        Dicts must all have the same keys in order for this function to pull the CSV headers.
            :param data:    A list of dicts with common keys.
            :return:        The CSV-formatted string.
        '''
        assert ValidateSchema.list_of_dicts(data, common_keys=True), '`data` must be list of dicts with common keys.'

        string_fh = StringIO()                                              # Create filehandler.
        writer = DictWriter(string_fh, data[0].keys())                      # Instantiate DictWriter.

        writer.writeheader()                                                # Write header row.
        writer.writerows(data)                                              # Write data rows.

        return string_fh.getvalue()

    @staticmethod
    def to_csv_file(
        data: list,
        out_file: Path
            ) -> NoReturn:
        '''
        Converts a list of dicts to CSV format and writes to a file.
        Dicts must all have the same keys in order for this function to pull the CSV headers.
            :param data:        A list of dicts with common keys.
            :param out_file:    The filepath to write the CSV data to.
        '''
        assert isinstance(out_file, Path), '`out_file` must be Path.'

        with open(out_file.with_suffix('.csv'), 'w', encoding='utf-8') as file:
            file.write(List.to_csv_str(data))                               # Write to file.
