# -*- coding: utf-8 -*-

from text_cleaner.processor.processor import merge_processors
from text_cleaner.processor.common import ASCII
from text_cleaner.processor.chinese import CHINESE


def test_demo():
    assert u'中文测试' == CHINESE.keep('中文测试')
    assert u'中文测试' == CHINESE.keep(u'中文测试')


def test_keep():
    raw = (
        u'NASA中文，由天文爱好者更新维护。'
        u'微信号：nasawatch。NASA中文的微博主页、个人资料、相册。'
        u'新浪微博，随时随地分享身边的新鲜事儿。'
    )
    expected = (
        u'中文，由天文爱好者更新维护。'
        u'微信号：。中文的微博主页、个人资料、相册。'
        u'新浪微博，随时随地分享身边的新鲜事儿。'
    )
    assert expected == CHINESE.keep(raw)

    CHINESE_WITH_ASCII = merge_processors(
        [CHINESE, ASCII],
    )
    assert raw == CHINESE_WITH_ASCII.keep(raw)
