#
# linter.py
# Linter for CudaLint
#
# Original: by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
# Change for CudaLint: Alexey T.
#
# License: MIT
#

"""This module exports the HtmlTidy plugin class."""

import os
from SublimeLinter.lint import Linter, util

if os.name=='nt':
    _exe = os.path.join(os.path.dirname(__file__), 'Tidy', 'tidy')
else:
    _exe = 'tidy'

class HtmlTidy(Linter):
    syntax = ('HTML', 'HTML_')
    cmd = (_exe, '-errors', '-quiet', '-utf8')

    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR
