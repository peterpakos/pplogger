# -*- coding: utf-8 -*-
"""Logging helper

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2018 WANdisco

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import logging


def get_logger(name=__name__,
               debug=False,
               verbose=False,
               quiet=False,
               level=logging.DEBUG,
               console_level=logging.INFO,
               file_level=False,
               log_file=None):
    if debug:
        name = ''

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if quiet:
        null_handler = logging.NullHandler()
        logger.addHandler(null_handler)
    else:
        if debug:
            fmt = '%(asctime)s [%(module)s] %(levelname)s %(message)s'
            console_formatter = logging.Formatter(fmt, datefmt='%Y-%m-%d %H:%M:%S')
        else:
            console_formatter = logging.Formatter('%(message)s')
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG if debug else console_level)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
        logging.getLogger().addHandler(logging.NullHandler())

    if file_level:
        if not log_file:
            log_file = os.path.join(
                os.path.abspath(os.path.curdir),
                os.path.splitext(sys.modules['__main__'].__file__)[0] + '.log'
            )

        file_formatter = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s %(message)s')
        try:
            file_handler = logging.FileHandler(log_file, mode='w')
            file_handler.setLevel(logging.DEBUG if debug else file_level)
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
        except (os.error.PermissionError, os.error.IsADirectoryError, os.error.FileNotFoundError) as e:
            logger.critical(e)
            exit(1)

    return logger
