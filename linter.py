# Copyright (c) 2013 Aparajita Fishman
# Change for CudaLint: Alexey T.
# License: MIT

import os
from cuda_lint import Linter, util

if os.name=='nt':
    _exe = os.path.join(os.path.dirname(__file__), 'tidy_win32', 'tidy')
else:
    _exe = 'tidy'

class HtmlTidy(Linter):
    syntax = ('HTML', 'HTML_')
    cmd = (_exe, '-errors', '-quiet', '-utf8')

    regex = r'^line (?P<line>\d+) column (?P<col>\d+) - (?:(?P<error>Error)|(?P<warning>Warning)): (?P<message>.+)'
    error_stream = util.STREAM_STDERR
