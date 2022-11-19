#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                _
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
# Author:       Casey Sparks
# Date:         November 15, 2022
# Notes:        Do not update this file directly. Rather, make changes to caseysparkz/__version__.py.
# Description:
'''Library of methods and APIs I use a lot.'''

from setuptools import (
    find_packages,
    setup
)
from caseysparkz import __version__

setup(
    name=__version__.__title__,
    description=__version__.__description__,
    author=__version__.__author__,
    author_email=__version__.__author_email__,
    version=__version__.__version__,
    url=__version__.__url__,
    install_requires=__version__.__requirements__,
    packages=find_packages(
        include=[
            __version__.__title__,
            f'{__version__.__title__}.*'
        ]
    )
)
