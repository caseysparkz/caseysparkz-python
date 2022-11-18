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
    Iterable,
    Union
)
from schema import (
    Schema,
    Optional,
    Or
)


log = getLogger(__name__)                                           # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                                    # Set locale.


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

        return schema.is_valid(data)                                # Validate the data against the schema.

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

        if not strict:                                              # Add optional arbitrary keys to dict.
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
            raise ValueError(':data: must be nested dictionaries with minimun depth 2.')

        else:
            type_class = Or(*allowed_types)
            d = {type_class: {type_class: type_class}}              # Depth 1.

            log.debug(f'Building nested dict schema of depth {depth}.')

            for i in range(depth - 1):                              # Generate nested dicts of arbitrary depth.
                data_schema = {type_class: d}

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
            raise ValueError(':param data: must be nested dictionaries with minimun depth 2.')

        else:
            type_class = Or(*allowed_types)
            d = {type_class: [type_class, Optional(type_class)]}    # Depth 1.

            log.debug(f'Building nested dict schema of depth {depth}.')

            for i in range(depth - 1):                              # Generate nested dicts of arbitrary depth.
                data_schema = {type_class: d}

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
            schema = Schema(                                        # List of flat dictionaries with common keys.
                [{
                    key: object
                    for key
                    in data[0].keys()                               # Base keys on first dict in list.
                }]
            )
        else:
            schema = Schema([dict])                                 # List of dicts.

        return Validate._arbitrary_schema(data, schema)

    @staticmethod
    def nested_iterable_has_depth(
        data: Iterable,
        depth: Union[int, None] = None,
        or_greater: bool = False,
        or_less: bool = False
            ) -> Union[int, bool]:
        '''
        Validate that a nested dictionary has a specified depth, or get the depth of a nested iterable.
            :param data:        The iterable to check.
            :param depth:       The depth to check for. Pass None to return the iterable's depth.
            :param or_greater:  If True, return True if depth is greater than this param.
            :param or_less:     If True, return True if depth is less than this param.
        '''
        dict_str = str(data)
        current_depth = 0
        max_depth = 0
        check = set()

        # Check params are valid.
        if (or_greater or or_less) and not depth:                   # Invalid params.
            return log.critical('You cannot pass :or_greater: or :or_less: without also passing :depth:.')

        elif or_greater and or_less:                                # Invalid params.
            return log.critical('Params :or_greater: and :or_less: are mutually exclusive.')

        else:                                                       # Valid params.
            pass

        # Iterate iterable and keep count of depth.
        for i in dict_str:
            if i in {'{', '[', '('}:                                # Opening parethesis.
                current_depth += 1                                  # Increase count of current depth.

                if current_depth > max_depth:
                    max_depth = current_depth                       # Increase count of max depth.

            elif i in {'{', '[', '('}:
                current_depth -= 1                                  # Decrease current depth.

            else:
                continue                                            # Do nothing.

        log.debug(f'Iterable depth: {max_depth}')
        log.debug(f'Iterable depth: {depth}')

        if depth:
            if or_greater:
                check = depth <= max_depth

            elif or_less:
                check = depth >= max_depth

            else:
                check = depth == max_depth

        else:
            check = max_depth

        return check
