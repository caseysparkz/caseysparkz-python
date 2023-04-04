#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''String manipulation.'''

from base64 import b64encode
from locale import setlocale, LC_ALL
from logging import getLogger

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.

log = getLogger(__name__)                                                   # Enable logging.


def to_b64_str(
    plaintext: str,
    encoding: str = 'utf-8'
        ) -> str:
    '''
    Convert a string to a base64-encoded string.
        :param plaintext:   The plaintext string to encode.
        :param encoding:    Encoding of the plaintext string.
        :return:            Base64-encoded string.
    '''
    return str(b64encode(plaintext.encode(encoding)), encoding)


def to_dict(
    plaintext: str,
    kv_separator: str = '=',
    obj_separator: str = '\r\n'
        ) -> dict:
    '''
    Converts a bash-like string of key-value pairs to a dict.
    Example structure: 'key1=value1\nkey2=value2\nkey3=value3'
        :param plaintext:       The string to format into a dictionary.
        :param kv_separator:    The string separating keys and values ('=').
        :param obj_separator:   The string separating key/value pairs ('\n').
        :return:                Python dict of dictstring.
    '''
    return {obj.split(kv_separator)[0]: obj.split(kv_separator)[1] for obj in plaintext.split(obj_separator)}
