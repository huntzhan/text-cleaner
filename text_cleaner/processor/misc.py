# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from text_cleaner.processor.processor import (
    RegexProcessor,
)


URL = RegexProcessor(
    r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}'
    r'\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
)


ESCAPED_WHITESPACE = RegexProcessor(
    r'[\\][ tnrfv]'
)
