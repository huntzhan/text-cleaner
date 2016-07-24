# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from text_cleaner.processor.processor import merge_processors


__all__ = [
    b'remove',
    b'keep',
]


_CACHED_MERGED_PROCESSORS = {}


def remove(text, processors):
    for processor in processors:
        text = processor.remove(text)
    return text


def keep(text, processors):
    key = tuple(processors)
    if key not in _CACHED_MERGED_PROCESSORS:
        _CACHED_MERGED_PROCESSORS[key] = merge_processors(key)

    processor = _CACHED_MERGED_PROCESSORS[key]
    return processor.keep(text)
