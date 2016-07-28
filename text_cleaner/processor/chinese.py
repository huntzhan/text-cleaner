# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from text_cleaner.processor.processor import (
    UnicodeRange,
    UnicodeRangeProcessor,
)
from text_cleaner.processor.common import (
    SYMBOLS_AND_PUNCTUATION_EXTENSION_RANGES,
)


# https://en.wikipedia.org/wiki/CJK_Unified_Ideographs

CJK_COMMON_RANGES = [
    UnicodeRange(0x4E00, 0x9FFF),
]

CJK_EXTENSION_RANGES = [
    UnicodeRange(0x3400, 0x4DFF),
    UnicodeRange(0x20000, 0x2A6DF),
    UnicodeRange(0x2A700, 0x2B73F),
    UnicodeRange(0x2B740, 0x2B81F),
    UnicodeRange(0x2B820, 0x2CEAF),
]

CJK_COMPATIBILITY_RANGES = [
    UnicodeRange(0x3300, 0x33FF),
    UnicodeRange(0xFE30, 0xFE4F),
    UnicodeRange(0xF900, 0xFAFF),
    UnicodeRange(0x2F800, 0x2FA1F),
]

# http://www.unicode.org/charts/PDF/U3000.pdf

CJK_SYMBOLS_AND_PUNCTUATION_RANGES = [
    UnicodeRange(0x3000, 0x303F),
]


# processors.

CHINESE_EXTENSION = UnicodeRangeProcessor(
    CJK_EXTENSION_RANGES,
)

CHINESE_COMPATIBILITY = UnicodeRangeProcessor(
    CJK_COMPATIBILITY_RANGES,
)

CHINESE_SYMBOLS_AND_PUNCTUATION = UnicodeRangeProcessor(
    CJK_SYMBOLS_AND_PUNCTUATION_RANGES,
)

# common usage.
CHINESE_CHARACTER = UnicodeRangeProcessor(
    CJK_COMMON_RANGES,
)

CHINESE = UnicodeRangeProcessor(
    CJK_COMMON_RANGES +
    CJK_SYMBOLS_AND_PUNCTUATION_RANGES +
    SYMBOLS_AND_PUNCTUATION_EXTENSION_RANGES,
)

# full version.
CHINESE_ALL = UnicodeRangeProcessor(
    CJK_COMMON_RANGES +
    CJK_EXTENSION_RANGES +
    CJK_COMPATIBILITY_RANGES +
    CJK_SYMBOLS_AND_PUNCTUATION_RANGES +
    SYMBOLS_AND_PUNCTUATION_EXTENSION_RANGES,
)
