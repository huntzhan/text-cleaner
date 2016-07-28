# -*- coding: utf-8 -*-
from text_cleaner.processor.common import (
    SYMBOLS_AND_PUNCTUATION,
    SYMBOLS_AND_PUNCTUATION_EXTENSION,
)


def test_symbol():

    raw = (
        u',.!@#&！!*($！&@!$！'
    )

    assert u' ！ ！ ！' == SYMBOLS_AND_PUNCTUATION.remove(raw)
    assert u' ' == SYMBOLS_AND_PUNCTUATION_EXTENSION.remove(raw)
