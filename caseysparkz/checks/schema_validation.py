#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Schema manipulation and validation.'''

from locale import setlocale, LC_ALL
from logging import getLogger
from typing import (
    Any as AnyType,
    Iterable as IterableType,
    List as ListType,
    Optional as OptionalType
)
from schema import (
    Optional,
    Or,
    Schema,
    SchemaError
)


LOG = getLogger(__name__)                                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.utf-8')                                            # Set locale.


class ValidateSchema():
    '''Validate various data schemas.'''
    @staticmethod
    def arbitrary_schema(
        data: AnyType,
        schema: Schema
            ) -> bool:
        '''
        ValidateSchema an arbitrary data object against a user-defined schema.
            :param data:    The data object to validate.
            :param schema:  The data schema to match.
            :return:        Boolean with the validity of the data schema.
        '''
        assert isinstance(schema, Schema), '`schema` must be Schema().'

        LOG.debug(f'Data:\n{data}')
        LOG.debug(f'Schema:\n{schema}')

        return schema.is_valid(data)                                        # Validate the data against the schema.

    @staticmethod
    def dict_contains_these_keys(
        data: dict,
        keys: set,
        strict: bool = False
            ) -> bool:
        '''
        Validate that a dictionary contains all specified keys.
            :param data:    The dictionary to validate.
            :param keys:    Set containing the keys to check for.
            :param strict:  Flag to ensure that the dictionary contains no additional keys.
            :return:        Boolean with the validity of the dict.
        '''
        data_schema = {                                                     # Dict of specified keys, arbitrary values.
            key: object
            for key
            in keys
        }

        if not strict:                                                      # Add optional arbitrary keys to dict.
            data_schema = data_schema | {Optional(object): object}

        return ValidateSchema.arbitrary_schema(data, Schema(data_schema))

    @staticmethod
    def dict_of_dicts(
        data: dict,
        depth: int = 2,
        allowed_types: OptionalType[set] = None
            ) -> bool:
        '''
        Validate that a data object is a list of dictionaries.
            :param data:            The object to validate.
            :param depth:           The depth of nested dictionaries to permit. (Eg 2: {obj: {obj: obj}})
            :param allowed_types:   Set containing allowed datatypes for keys (and leaf values).
            :return:                Boolean with the validity of the dict.
        '''
        is_dict = isinstance(data, dict)
        min_depth = depth >= 2

        assert is_dict, '`data` must be dict.'
        assert min_depth, '`depth` must be >= 2.'

        if not all([is_dict, min_depth]):
            raise SchemaError(':data: must be nested dictionaries with minimun depth 2.')

        if not allowed_types:
            allowed_types = {str, int, float}

        type_class = Or(*allowed_types)
        data_schema = {type_class: {type_class: type_class}}                # Depth 1.
        current_schema_depth = 2

        LOG.debug(f'Building nested dict schema of depth {depth}.')

        while current_schema_depth < depth:                                 # Generate nested dicts of arbitrary depth.
            data_schema = {type_class: data_schema}
            current_schema_depth += 1

        return ValidateSchema.arbitrary_schema(data, Schema(data_schema))

    @staticmethod
    def list_items_unique(
        list_obj: ListType[AnyType]
            ) -> bool:
        '''
        Validate that a list contains no duplicate items.
            :param list_obj:    The list to check for duplicates.
            :return:            Boolean with the validity of the list.
        '''
        return len(set(list_obj)) == len(list_obj)

    @staticmethod
    def list_of_dicts(
        data: ListType[dict],
        common_keys: bool = False
            ) -> bool:
        '''
        Validate that a data object is a list of flat dictionaries.
            :param data:        The object to validate.
            :param common_keys: Validate that every dictionary has identical keys.
            :return:            Boolean with the validity of the list.
        '''
        list_items_are_dicts = [isinstance(item, dict) for item in data]
        keys_identical = [item.keys() == data[0].keys() for item in data]

        assert isinstance(data, list), '`data` must be list.'
        assert all(list_items_are_dicts), '`data` must contain only dicts.'

        if common_keys:
            assert all(keys_identical), 'All `data` dict keys must be identical.'

            schema = Schema([{                                              # List of flat dicts with common keys.
                key: object
                for key
                in data[0].keys()                                           # Base keys on first dict in list.
            }])
        else:
            schema = Schema([dict])                                         # List of dicts.

        return ValidateSchema.arbitrary_schema(data, schema)

    @staticmethod
    def max_iterable_depth(
        data: IterableType
            ) -> int:
        '''
        Get the maximum depth of a nested iterable.
            :param data:    The iterable to check.
            :return:        Maximum depth found in the iterable.
        '''
        current_depth = 0
        max_depth = 0
        open_parens = {'(', '{', '['}                                       # Possible opening parens.
        paren_str = ''.join(                                                # Produces str like '[{()()}{[]}]'.
            char
            for char
            in str(data)                                                    # Convert arbitrary type to str.
            if char in open_parens.union({')', '}', ']'})                   # All possible opening/closing parens.
        )

        for char in paren_str:                                              # Iterate iterable and keep count of depth.
            if char in open_parens:
                current_depth += 1                                          # Increase count of current depth.
                max_depth = max(max_depth, current_depth)                   # Set max depth.

            else:
                current_depth -= 1                                          # Decrease current depth.

        if current_depth != 0:                                              # Total closing should = total opening.
            raise StopIteration(f'Iterable is invalid. Depth: {current_depth}')

        LOG.debug(f'Maximum iterable depth: {max_depth}')

        return max_depth
