#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Schema manipulation and validation.'''

from locale import setlocale, LC_ALL
from logging import getLogger
from typing import Any
from schema import Schema


log = getLogger(__name__)                               # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                        # Set locale.


class Validate():
    '''Validate various data schemas.'''
    @staticmethod
    def _generic_schema(
        data: Any,
        schema: Schema
            ) -> bool:
        '''
        Validate an arbitrary data model against a user-defined schema.
            :param data:    The data model to validate.
            :param schema:  The data schema to match.
        '''
        return schema.is_valid(data)                    # Validate the data against the schema.

    @staticmethod
    def list_of_dicts(
        data: list,
        common_keys: bool = False
            ) -> bool:
        '''
        Validate that a data object is a list of dictionaries.
            :param data:        The object to validate.
            :param common_keys: Validate that every dictionary has identical keys.
        '''
        if common_keys:
            schema = Schema(                            # List of dicts with common keys.
                [{
                    key: object
                    for key
                    in data[0].keys()                   # Base keys on first dict in list.
                }]
            )
        else:
            schema = Schema([dict])                     # List of dicts.

        return Validate._generic_schema(data, schema)
