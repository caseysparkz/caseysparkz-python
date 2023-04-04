#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:       Casey Sparks
# Date:         November 17, 2022
# Description:
'''System manipulation and checks.'''

from logging import getLogger
from locale import setlocale, LC_ALL
from psutil import process_iter


log = getLogger(__name__)                                                   # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                                            # Set locale.


class Check():
    '''Misc. system checks.'''
    @staticmethod
    def process_running(
        process_name: str
            ) -> bool:
        '''
        Check that a process is running on the system.
            :param process_name:    The (case-sensitive) name of the process to check for.
        '''
        log.debug(f'Checking for process {process_name}.')

        return process_name in [proc.name() for proc in process_iter()]
