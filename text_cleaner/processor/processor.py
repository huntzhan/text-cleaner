# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

import re


DEFAULT_REPLACE_TEXT = ' '


def join_regexes(regexes, delimiter='|'):
    return delimiter.join(regexes)


def merge_processors(processors, replace_text=DEFAULT_REPLACE_TEXT):
    regexes = [p.regex for p in processors]
    return RegexProcessor(
        join_regexes(regexes), replace_text,
    )


def decode(text):
    if isinstance(text, bytes):
        return text.decode('utf-8')
    else:
        return text


def force_unicode(method):

    def _wrapper(self, text):

        text = decode(text)
        return method(self, text)

    return _wrapper


class UnicodeRange(object):

    def __init__(self, begin, end):
        self.begin = int(begin)
        self.end = int(end)

    @property
    def regex(self):
        # 1. str, for formatting.
        pattern = '\\U{begin:0>8X}-\\U{end:0>8X}'.format(
            begin=self.begin, end=self.end,
        )
        # 2. to bytes.
        pattern = pattern.encode('utf-8')
        # 3. decode to str.
        return pattern.decode('unicode_escape')


class RegexProcessor(object):

    def __init__(self, regex, replace_text=DEFAULT_REPLACE_TEXT):
        # force unicode.
        self._regex = decode(regex)
        self._replace_text = decode(replace_text)

        self._regex_obj = re.compile(self.regex, re.UNICODE)

    @property
    def regex(self):
        return self._regex

    @property
    def replace_text(self):
        return self._replace_text

    def copy(self):
        return RegexProcessor(self.regex, self.replace_text)

    @force_unicode
    def replace(self, new_replace_text):
        obj = self.copy()
        obj._replace_text = new_replace_text
        return obj

    @force_unicode
    def remove(self, text):
        return self._regex_obj.sub(
            self._replace_text,
            text,
        )

    @force_unicode
    def keep(self, text):
        return self._replace_text.join(
            # force non-capture.
            m.group() for m in self._regex_obj.finditer(text),
        )

    @force_unicode
    def verify(self, text):
        match = self._regex_obj.match(text)
        if match is None:
            return False
        else:
            return match.group() == text


class UnicodeRangeProcessor(RegexProcessor):

    def __init__(self, ranges, replace_text=DEFAULT_REPLACE_TEXT):
        self._ranges = ranges

        super().__init__(
            self.ranges_to_regex(ranges),
            replace_text,
        )

    def ranges_to_regex(self, ranges):
        joined = join_regexes(
            map(lambda ur: ur.regex, ranges),
            delimiter='',
        )
        return r'[{0}]+'.format(joined)

    def copy(self):
        return UnicodeRangeProcessor(self._ranges, self.replace_text)
