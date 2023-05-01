#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Dictionary manipulation.'''

from locale import setlocale, LC_ALL
from logging import getLogger
from io import StringIO
from configparser import ConfigParser
from dict2xml import dict2xml
from schema import SchemaError
from ..checks.schema_validation import ValidateSchema


LOG = getLogger(__name__)                                                   # Instantiate parser.

setlocale(LC_ALL, 'en_US.utf-8')                                            # Set locale.

class Dict():
    '''Methods for manipulating dictionaries.'''
    @staticmethod
    def to_html(
        data: dict
            ) -> str:
        '''
        Converts a dictionary to a single string with user-defined delineators.
            :param data:    The dictionary to format into INI.
            :return:        HTML-data of dict.
        '''
        assert isinstance(data, dict), '`data` must be dict.'

        return dict2xml(data)

    @staticmethod
    def to_ini(
        data: dict,
        space_around_delimiters: bool = True
            ) -> str:
        '''
        Converts a dictionary to a single string with user-defined delineators.
            :param data:                    The dictionary to format into INI.
            :param space_around_delimiters: Surround key/value delimiters with spaces.
            :return:                        INI of dict.
        '''
        assert isinstance(data, dict), '`data` must be dict.'
        assert isinstance(space_around_delimiters, bool), '`space_around_delimiters` must be bool.'

        if ValidateSchema.dict_of_dicts(data, depth=2):
            config = ConfigParser()
            config._sections = data
            string_fh = StringIO()

            config.write(string_fh, space_around_delimiters=space_around_delimiters)

            return string_fh.getvalue()

        raise SchemaError(':param data: must be a flat dictionary.')

    @staticmethod
    def to_string(
        data: dict,
        kv_separator: str = '=',
        object_separator: str = '\n'
            ) -> str:
        '''
        Converts a dictionary to a single string with user-defined delineators.
            :param data:                The dictionary to format into a string.
            :param kv_separator:        The string separating keys and values.
            :param object_separator:    The string separating key/value pairs.
            :return:                    Bash-like dict of K/V pairs.
        '''
        assert isinstance(data, dict), '`data` must be dict.'
        assert isinstance(kv_separator, str), '`kv_separator` must be str.'
        assert isinstance(object_separator, str), '`object_separator` must be str.'

        return object_separator.join([f'{key}{kv_separator}{data[key]}' for key in data])

    @staticmethod
    def to_xml(
        data: dict
            ) -> str:
        '''
        Converts a dictionary to an XML string.
            :param data:    The dictionary to format into INI.
            :return:        XML data of dict.
        '''
        assert isinstance(data, dict), '`data` must be dict.'

        return dict2xml(data)
