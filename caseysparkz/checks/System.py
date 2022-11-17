#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
# Author:       Casey Sparks
# Date:         November 17, 2022
# Description:
'''System manipulation and checks.'''

from logging import getLogger
from locale import setlocale, LC_ALL
from psutil import process_iter


log = getLogger(__name__)                               # Instantiate logger.

setlocale(LC_ALL, 'en_US.UTF-8')                        # Set locale.


class Check():
    @staticmethod
    def process_running(
        process_name: str
            ) -> bool:
        '''
        Check that a process is running on the system.
            :param process_name:    The name of the process to check for.
        '''
        log.debug(f'Checking for process {process_name}.')

        return process_name.lower() in [proc.name().lower() for proc in process_iter()]
