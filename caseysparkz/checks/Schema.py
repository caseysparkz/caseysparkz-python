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
'''Schema manipulation and validation.'''

from locale import setlocale, LC_ALL
from logging import getLogger
from typing import (
    Any,
    Iterable
)
from schema import (
    Schema,
    SchemaError,
    Optional,
    Or
)


log = getLogger(__name__)                                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.


class Validate():
    '''Validate various data schemas.'''
    def _arbitrary_schema(
        data: Any,
        schema: Schema
            ) -> bool:
        '''
        Validate an arbitrary data object against a user-defined schema.
            :param data:    The data object to validate.
            :param schema:  The data schema to match.
        '''
        log.debug(f'Data:\n{data}')
        log.debug(f'Schema:\n{schema}')

        return schema.is_valid(data)                                        # Validate the data against the schema.

    @staticmethod
    def dict_contains_these_keys(
        data: dict,
        keys: Iterable,
        strict: bool = False
            ) -> bool:
        '''
        Validate that a dictionary contains all specified keys.
            :param data:    The dictionary to validate.
            :param keys:    Iterable containing the keys to check for.
            :param strict:  Flag to ensure that the dictionary contains no additional keys.
        '''
        data_schema = {
            key: object
            for key
            in keys
        }

        if not strict:                                                      # Add optional arbitrary keys to dict.
            data_schema = data_schema | {Optional(object): object}

        return Validate._arbitrary_schema(data, Schema(data_schema))

    @staticmethod
    def dict_of_dicts(
        data: dict,
        depth: int = 2,
        allowed_types: Iterable = (str, int, float)
            ) -> bool:
        '''
        Validate that a data object is a list of dictionaries.
            :param data:            The object to validate.
            :param depth:           The depth of nested dictionaries to permit. (Eg 2: {obj: {obj: obj}})
            :param allowed_types:   Iterable containing allowed datatypes for keys (and leaf values).
        '''
        if depth < 2:
            raise SchemaError(':data: must be nested dictionaries with minimun depth 2.')

        else:
            type_class = Or(*allowed_types)
            data_schema = {type_class: {type_class: type_class}}            # Depth 1.

            log.debug(f'Building nested dict schema of depth {depth}.')

            for i in range(depth - 1):                                      # Generate nested dicts of arbitrary depth.
                data_schema = {type_class: data_schema}

        return Validate._arbitrary_schema(data, Schema(data_schema))

    @staticmethod
    def dict_of_lists(
        data: list,
        depth: int = 2,
        allowed_types: Iterable = (str, int, float)
            ) -> bool:
        '''
        Validate that a data object is a list of dictionaries.
            :param data:            The object to validate.
            :param depth:           The depth of nested dictionaries to permit. (Eg 2: {obj: {obj: obj}})
            :param allowed_types:   Iterable containing allowed datatypes for keys (and leaf values).
        '''
        if depth < 2:
            raise SchemaError(':param data: must be nested dictionaries with minimun depth 2.')

        else:
            type_class = Or(*allowed_types)
            data_schema = {type_class: [type_class, Optional(type_class)]}  # Depth 1.

            log.debug(f'Building nested dict schema of depth {depth}.')

            for i in range(depth - 1):                                      # Generate nested dicts of arbitrary depth.
                data_schema = {type_class: data_schema}

        return Validate._arbitrary_schema(data, Schema(data_schema))

    @staticmethod
    def list_of_dicts(
        data: list,
        common_keys: bool = False
            ) -> bool:
        '''
        Validate that a data object is a list of flat dictionaries.
            :param data:        The object to validate.
            :param common_keys: Validate that every dictionary has identical keys.
        '''
        if common_keys:
            schema = Schema(                                                # List of flat dicts with common keys.
                [{
                    key: object
                    for key
                    in data[0].keys()                                       # Base keys on first dict in list.
                }]
            )
        else:
            schema = Schema([dict])                                         # List of dicts.

        return Validate._arbitrary_schema(data, schema)

    @staticmethod
    def max_iterable_depth(
        data: Iterable
            ) -> int:
        '''
        Get the maximum depth of a nested iterable.
            :param data:        The iterable to check.
        '''
        dict_str = str(data)
        current_depth = 0
        max_depth = 0

        for char in dict_str:                                               # Iterate iterable and keep count of depth.
            if char in {'{', '[', '('}:                                     # Opening parethesis.
                current_depth += 1                                          # Increase count of current depth.

                if current_depth > max_depth:
                    max_depth = current_depth                               # Increase count of max depth.

            elif char in {'}', ']', ')'}:
                current_depth -= 1                                          # Decrease current depth.

            else:
                continue                                                    # Do nothing.

        log.debug(f'Iterable depth: {max_depth}')

        return max_depth
