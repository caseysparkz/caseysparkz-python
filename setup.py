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
from caseysparkz.__init__ import (
    __title__,
    __description__,
    __author__,
    __author_email__,
    __url__,
    __version__,
    __licence__,
    __python_requires__,
    __requirements__
)

setup(
    name=__title__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    licence=__licence__,
    url=__url__,
    install_requires=__requirements__,
    python_requires=__python_requires__,
    packages=find_packages(include=[__title__, f'{__title__}.*'])
)
