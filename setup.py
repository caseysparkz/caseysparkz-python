#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
# / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
#| (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
# \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                    |___/    |_|
# Author:       Casey Sparks
# Date:         November 15, 2022
# Description:
'''Library of methods and APIs I use a lot.'''

from setuptools import setup, find_packages
from caseysparkz import (
    __title__,
    __description__,
    __author__,
    __author_email__,
    __version__,
    __url__
)


setup(
    name=__title__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    version=__version__,
    url=__url__,
    packages=find_packages(include=[
        'caseysparkz',
        'caseysparkz.*'
    ]),
    install_requires=[
        'ratelimit>=2.2.0',
        'requests>=2.26.0'
    ]
)
