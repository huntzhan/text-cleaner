# -*- coding: utf-8 -*-

from text_cleaner.processor.misc import URL, ESCAPED_WHITESPACE


URL = URL.replace('TCURL')


def test_url():

    raw = (
        '点击http://t.cn/RtU0mZ1 查看'
    )
    expected = (
        u'点击TCURL 查看'
    )

    assert expected == URL.remove(raw)


def test_escaped_whitespace():

    raw = (
        '点击\\nhttp://t.cn/RtU0mZ1 \\t查看'
    )
    expected = (
        u'点击 http://t.cn/RtU0mZ1  查看'
    )

    assert expected == ESCAPED_WHITESPACE.remove(raw)
