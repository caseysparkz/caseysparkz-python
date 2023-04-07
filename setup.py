#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                _
#   ___ __ _ ___  ___ _   _ ___ _ __   __ _ _ __| | __ ____
#  / __/ _` / __|/ _ \ | | / __| '_ \ / _` | '__| |/ /|_  /
# | (_| (_| \__ \  __/ |_| \__ \ |_) | (_| | | _|   <  / /
#  \___\__,_|___/\___|\__, |___/ .__/ \__,_|_|(_)_|\_\/___|
#                     |___/    |_|
#
# Author:       Casey Sparks
# Date:         November 15, 2022
'''Library of methods and APIs I use a lot.'''

from setuptools import (
    find_packages,
    setup
)

# Make changes below.
NAME = 'caseysparkz'
AUTHOR = 'caseyspar.kz'
AUTHOR_EMAIL = 'python@caseyspar.kz'
DESCRIPTION = 'Library of methods and APIs I use a lot.'
LICENSE = 'GPL-2.0-or-later'
PACKAGES = find_packages(include=[NAME, f'{NAME}.*'])
PYTHON_REQUIRES = '>=3.10'
URL = 'https://github.com/caseysparkz/python-caseysparkz'
VERSION = '0.0.2'                                                           # Increment version.
INSTALL_REQUIRES = [                                                        # Update requirements.
    'dict2xml>=1.7.3,<2.0.0',
    'psutil>=5.9.4,<6.0.0',
    'schema>=0.7.0,<1.0.0'
]

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    name=NAME,
    packages=PACKAGES,
    python_requires=PYTHON_REQUIRES,
    url=URL,
    version=VERSION
)
