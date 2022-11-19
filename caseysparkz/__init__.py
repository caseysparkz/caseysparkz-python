#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
# Author:       Casey Sparks
# Date:         November 15, 2022

from . import (
    checks,
    data_manipulation
)

__all__ = [
    'checks',
    'data_manipulation'
]


# User-defined exceptions.
class MutuallyInclusiveArgumentError(Exception):
    def __init__(
        self,
        error_message: str = 'Arguments missing from function call.'
            ):
        '''Raises an exception if an argument is missing from a function.'''
        self.error_message = error_message

        super().__init__(self.error_message)


class MutuallyExclusiveArgumentError(Exception):
    def __init__(
        self,
        error_message: str = 'Arguments are mutually exclusive.'
            ):
        '''Raises an exception if two mutually exclusive arguments are passed to a function.'''
        self.error_message = error_message

        super().__init__(self.error_message)
