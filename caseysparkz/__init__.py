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

from . import (
    checks,
    data_manipulation
)

__title__ = 'caseysparkz'
__description__ = 'Library of methods and APIs I use a lot.'
__author__ = 'caseyspar.kz'
__author_email__ = 'python@caseyspar.kz'
__url__ = 'https://github.com/caseysparkz/python-caseysparkz'
__version__ = '2.0.0'
__licence__ = 'GPL-2.0-or-later'
__python_requires__ = '>=3.10'
__requirements__ = [
    'dict2xml>=1.7.3,<2.0.0',
    'psutil>=5.9.4,<6.0.0',
    'schema<1.0.0>=0.7.0'
]
__all__ = [
    'checks',
    'data_manipulation'
]


# User-defined exceptions.
class MutuallyInclusiveArgumentError(Exception):
    '''Raises an exception if an argument is missing from a function.'''
    def __init__(
        self,
        error_message: str = 'Arguments missing from function call.'
            ):
        '''
            :param error_message: The message to raise with the exception.
        '''
        super().__init__(error_message)


class MutuallyExclusiveArgumentError(Exception):
    '''Raises an exception if two mutually exclusive arguments are passed to a function.'''
    def __init__(
        self,
        error_message: str = 'Arguments are mutually exclusive.'
            ):
        '''
            :param error_message: The message to raise with the exception.
        '''
        super().__init__(error_message)
