# -*- coding: utf-8 -*-

from text_cleaner.processor.common import ASCII
from text_cleaner.processor.chinese import CHINESE
from text_cleaner.processor.misc import URL

from text_cleaner import remove, keep


def test_remove():
    raw = (
        '点击http://t.cn/RtU0mZ1 查看,123456,test'
    )
    expected = (
        u'点击  查看 '
    )

    assert expected == remove(raw, [URL, ASCII])


def test_keep():
    raw = (
        '点击http://t.cn/RtU0mZ1 查看,123456,test'
    )
    expected = (
        u'点击 查看'
    )

    assert expected == keep(raw, [CHINESE])


def test_keep_with_cache():
    raw = (
        '点击http://t.cn/RtU0mZ1 查看,123456,test'
    )
    expected = (
        u'点击 http://t.cn/RtU0mZ1 查看'
    )

    assert expected == keep(raw, [CHINESE, URL])
    assert expected == keep(raw, [CHINESE, URL])
