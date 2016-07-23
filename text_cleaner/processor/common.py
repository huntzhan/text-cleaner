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


# basic.

ASCII_ALPHA_RANGES = [
    UnicodeRange(0x0041, 0x005A),
    UnicodeRange(0x0061, 0x007A),
]

ASCII_DIGIT_RANGES = [
    UnicodeRange(0x0030, 0x0039),
]

ASCII_SYMBOLS_AND_PUNCTUATION_RANGES = [
    UnicodeRange(0x0021, 0x002F),
    UnicodeRange(0x003A, 0x0040),
    UnicodeRange(0x005B, 0x0060),
    UnicodeRange(0x007B, 0x007E),
]


# extension.

ALPHA_EXTENSION_RANGES = [
    UnicodeRange(0xFF21, 0xFF3A),
    UnicodeRange(0xFF41, 0xFF5A),
]

DIGIT_EXTENSION_RANGES = [
    UnicodeRange(0xFF10, 0xFF19),
]

SYMBOLS_AND_PUNCTUATION_EXTENSION_RANGES = [
    UnicodeRange(0xFF00, 0xFF0F),
    UnicodeRange(0xFF1A, 0xFF20),
    UnicodeRange(0xFF3B, 0xFF40),
    UnicodeRange(0xFF5B, 0xFF64),
    UnicodeRange(0xFFE0, 0xFFEE),
]


# processor.
ALPHA = UnicodeRangeProcessor(
    ASCII_ALPHA_RANGES,
)
DIGIT = UnicodeRangeProcessor(
    ASCII_DIGIT_RANGES,
)
SYMBOLS_AND_PUNCTUATION = UnicodeRangeProcessor(
    ASCII_SYMBOLS_AND_PUNCTUATION_RANGES,
)
ASCII = UnicodeRangeProcessor(
    ASCII_ALPHA_RANGES +
    ASCII_DIGIT_RANGES +
    ASCII_SYMBOLS_AND_PUNCTUATION_RANGES,
)


ALPHA_EXTENSION = UnicodeRangeProcessor(
    ASCII_ALPHA_RANGES +
    ALPHA_EXTENSION_RANGES,
)
DIGIT_EXTENSION = UnicodeRangeProcessor(
    ASCII_DIGIT_RANGES +
    DIGIT_EXTENSION_RANGES,
)
SYMBOLS_AND_PUNCTUATION_EXTENSION = UnicodeRangeProcessor(
    ASCII_SYMBOLS_AND_PUNCTUATION_RANGES +
    SYMBOLS_AND_PUNCTUATION_EXTENSION_RANGES,
)
