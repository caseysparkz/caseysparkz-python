#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
# Author:       Casey Sparks
# Date:         November 15, 2022
'''Python tooling that I use a lot.'''

from types import ModuleType
from typing import List
from . import (
    checks,
    data_manipulation
)

__all__ = [
    key
    for key
    in globals()
    if isinstance(globals()[key], ModuleType)
    and not key.startswith('_')
]


# Custom exceptions.
class MutuallyInclusiveArgumentError(Exception):
    '''Raises an exception if a mutually inclusive argument is missing from a function.'''
    def __init__(
        self,
        missing_arguments: List[str],
        error_message: str = 'Arguments missing from function call.'
            ):
        '''
            :param missing_arguments:   A list of missing arguments.
            :param error_message:       The message to raise with the exception.
        '''
        strings_in_list = [isinstance(obj, str) for obj in missing_arguments]

        assert isinstance(missing_arguments, list), '`missing_arguments` must be list of strings.'
        assert all(strings_in_list), '`missing_arguments` must be list of strings.'
        assert isinstance(error_message, list), '`error_message` must be str.'

        super().__init__(f'{error_message} Missing arguments: {missing_arguments}')


class MutuallyExclusiveArgumentError(Exception):
    '''Raises an exception if two mutually exclusive arguments are passed to a function.'''
    def __init__(
        self,
        argument_1_name: str,
        argument_2_name: str,
        error_message: str = 'Arguments are mutually exclusive.'
            ):
        '''
            :param argument_1:      The first mutually exclusive argument.
            :param argument_2:      The second mutually exclusive argument.
            :param error_message:   The message to raise with the exception.
        '''
        assert isinstance(argument_1_name, str), '`argument_1_name` must be str.'
        assert isinstance(argument_2_name, str), '`argument_2_name` must be str.'
        assert isinstance(error_message, str), '`error_message` must be str.'

        super().__init__(f'{error_message} Arg1: {argument_1_name}, Arg2: {argument_2_name}')
