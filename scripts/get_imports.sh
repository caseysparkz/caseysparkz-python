#!/usr/bin/env bash
# Author:       Casey Sparks
# Date:         April 11, 2023
# Description:  Get all requirements.

GIT_DIR=$(git rev-parse --show-toplevel)/caseysparkz

grep -R import ${GIT_DIR}/*                                                     \
    | sed -E 's/^.*:(from|import)\s//g'                                         \
    | sed -E 's/\s.*$//g'                                                       \
    | grep -vE '^\.'                                                            \
    | sort -u
