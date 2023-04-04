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


log = getLogger(__name__)                                                   # Instantiate parser.

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.


def to_html(
    data: dict
        ) -> str:
    '''
    Converts a dictionary to a single string with user-defined delineators.
        :param data:    The dictionary to format into INI.
        :return:        HTML-data of dict.
    '''
    return dict2xml(data)


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
    if ValidateSchema.dict_of_dicts(data, depth=2):
        config = ConfigParser()
        config._sections = data
        string_fh = StringIO()

        config.write(string_fh, space_around_delimiters=space_around_delimiters)

        return string_fh.getvalue()

    raise SchemaError(':param data: must be a flat dictionary.')


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
    return object_separator.join([f'{key}{kv_separator}{data[key]}' for key in data])


def to_xml(
    data: dict
        ) -> str:
    '''
    Converts a dictionary to a single string with user-defined delineators.
        :param data:    The dictionary to format into INI.
        :return:        XML data of dict.
    '''
    return dict2xml(data)
