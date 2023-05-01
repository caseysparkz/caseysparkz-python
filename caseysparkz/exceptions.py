#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
# Author:       Casey Sparks
# Date:         November 15, 2022
'''Custom exceptions.'''

from logging import getLogger
from typing import List

LOG = getLogger(__name__)


class MutuallyInclusiveArgumentError(Exception):
    '''Raises an exception if a mutually inclusive argument is missing from a function.'''
    def __init__(
        self,
        mutinc_args: List[str],
        error_message: str = 'Arguments missing from function call.'
            ):
        '''
        :param mutinc_args:     A list of mutually inclusive arguments.
        :param error_message:   The message to raise with the exception.
        '''
        assert isinstance(mutinc_args, list), '`mutinc_args` must be list.'
        assert all(isinstance(obj, str) for obj in mutinc_args), '`mutinc_args` must be list of strings.'
        assert isinstance(error_message, str), '`error_message` must be str.'
        super().__init__(f'{error_message} Mutually inclusive arguments: `{", ".join(mutinc_args)}`')


class MutuallyExclusiveArgumentError(Exception):
    '''Raises an exception if two mutually exclusive arguments are passed to a function.'''
    def __init__(
        self,
        mutex_args: list,
        error_message: str = 'Arguments are mutually exclusive.'
            ):
        '''
        :param mutex_args:      A list of mutually exclusive arguments.
        :param error_message:   The message to raise with the exception.
        '''
        assert isinstance(mutex_args, list), '`mutex_args` must be list.'
        assert all(isinstance(obj, str) for obj in mutex_args), '`mutex_args` must be list of strings.'
        assert isinstance(error_message, str), '`error_message` must be str.'
        super().__init__(f'{error_message} Mutually exclusive arguments: `{", ".join(mutex_args)}`.')
