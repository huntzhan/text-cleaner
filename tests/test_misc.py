# -*- coding: utf-8 -*-

from text_cleaner.processor.misc import (
    URL,
    ESCAPED_WHITESPACE,
    WECHAT_EMOJI_EN,
    WECHAT_EMOJI_ZHCN,
    WECHAT_EMOJI,
)


URL = URL.replace('TCURL')


def test_url():

    raw = (
        '点击http://t.cn/RtU0mZ1 查看'
    )
    expected = (
        u'点击TCURL 查看'
    )

    assert expected == URL.remove(raw)

    raw = (
        '点击http://173.255.0.1/browser.php?u=test 查看'
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


def test_wechat_emoji():

    raw = (
        '[Smile][微笑][这不是表情][not an emoji]'
    )
    expected = (
        u' [微笑][这不是表情][not an emoji]'
    )

    assert expected == WECHAT_EMOJI_EN.remove(raw)

    raw = (
        '[Smile][微笑][这不是表情][not an emoji]'
    )
    expected = (
        u'[Smile] [这不是表情][not an emoji]'
    )

    assert expected == WECHAT_EMOJI_ZHCN.remove(raw)

    raw = (
        '[Smile][微笑][这不是表情][not an emoji]'
    )
    expected = (
        u'  [这不是表情][not an emoji]'
    )

    assert expected == WECHAT_EMOJI.remove(raw)
