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
'''String manipulation.'''


from base64 import b64encode
from locale import setlocale, LC_ALL
from logging import getLogger

setlocale(LC_ALL, 'en_US.UTF-8')                                    # Set locale.

log = getLogger(__name__)                                           # Enable logging.


def to_b64_str(
    plaintext: str
        ) -> str:
    '''
    Convert a string to a base64-encoded string.
        :param plaintext: The base64-encoded string to decode.
    '''
    return str(b64encode(plaintext.encode('utf-8')), 'utf-8')


def to_dict(
    plaintext: str,
    kv_separater: str = '=',
    object_separator: str = '\r\n'
        ) -> dict:
    '''
    Converts a bash-like string of key-value pairs to a dict.
    Example structure: 'key1=value1\nkey2=value2\nkey3=value3'
        :param plaintext:           The string to format into a dictionary.
        :param kv_separator:        The string separating keys and values ('=').
        :param object_separator:    The string separating key/value pairs ('\n').
    '''
    output_dict = {
        obj.split('kv_separator')[0]: obj.split('kv_separator')[1]
        for obj
        in plaintext.split('object_separator')
    }

    log.debug(output_dict)

    return output_dict
