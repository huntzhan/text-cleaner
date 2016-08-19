# -*- coding: utf-8 -*-
from __future__ import (
    division, absolute_import, print_function, unicode_literals,
)
from builtins import *                  # noqa
from future.builtins.disabled import *  # noqa

from text_cleaner.processor.processor import (
    RegexProcessor,
)


_URL_PATTERN_PREFIX = (
    # https://mathiasbynens.be/demo/url-regex
    # https://gist.github.com/dperini/729294

    # protocol identifier
    '(?:(?:https?|ftp)://)'
    # user:pass authentication
    '(?:\S+(?::\S*)?@)?'
    '(?:'
    # IP address exclusion
    # private & local networks
    '(?!(?:10|127)(?:\.\d{1,3}){3})'
    '(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})'
    '(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})'
    # IP address dotted notation octets
    # excludes loopback network 0.0.0.0
    # excludes reserved space >= 224.0.0.0
    # excludes network & broadcast addresses
    # (first & last IP address of each class)
    '(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])'
    '(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}'
    '(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))'
    '|'
    # host name
    '(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)'

    # domain name
    # '(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*'
    # http://stackoverflow.com/questions/8010005/python-re-infinite-execution
    # http://www.regular-expressions.info/catastrophic.html
    '(?:[a-z\u00a1-\uffff0-9\-\.]*)'

    # TLD identifier
    '(?:\.(?:[a-z\u00a1-\uffff]{2,}))'
    ')'
    # port number
    '(?::\d{2,5})?'
)


URL = RegexProcessor(
    _URL_PATTERN_PREFIX +
    # resource path, any non-whitespace of unicode.
    '(?:/\S*)?'
)

RESTRICT_URL = RegexProcessor(
    _URL_PATTERN_PREFIX +
    # resource path, any non-whitespace of ascii.
    '(?:/[!-~]*)?'
)


ESCAPED_WHITESPACE = RegexProcessor(
    r'[\\][ tnrfv]'
)


_WECHAT_EMOJI_EN = [
    'Smile',
    'Grimace',
    'Drool',
    'Scowl',
    'CoolGuy',
    'Sob',
    'Shy',
    'Silent',
    'Sleep',
    'Cry',
    'Awkward',
    'Angry',
    'Tongue',
    'Grin',
    'Surprise',
    'Frown',
    'Ruthless',
    'Blush',
    'Scream',
    'Puke',
    'Chuckle',
    'Joyful',
    'Slight',
    'Smug',
    'Hungry',
    'Drowsy',
    'Panic',
    'Sweat',
    'Laugh',
    'Commando',
    'Determined',
    'Scold',
    'Shocked',
    'Shhh',
    'Dizzy',
    'Tormented',
    'Toasted',
    'Skull',
    'Hammer',
    'Wave',
    'Speechless',
    'NosePick',
    'Clap',
    'Shame',
    'Trick',
    'Bah！L',
    'Bah！R',
    'Yawn',
    'Pooh-pooh',
    'Shrunken',
    'TearingUp',
    'Sly',
    'Kiss',
    'Wrath',
    'Whimper',
    'Cleaver',
    'Watermelon',
    'Beer',
    'Basketball',
    'PingPong',
    'Coffee',
    'Rice',
    'Pig',
    'Rose',
    'Wilt',
    'Lips',
    'Heart',
    'BrokenHeart',
    'Cake',
    'Lightning',
    'Bomb',
    'Dagger',
    'Soccer',
    'Ladybug',
    'Poop',
    'Moon',
    'Sun',
    'Gift',
    'Hug',
    'ThumbsUp',
    'ThumbsDown',
    'Shake',
    'Peace',
    'Fight',
    'Beckon',
    'Fist',
    'Pinky',
    'RockOn',
    'Nuh-uh',
    'OK',
    'InLove',
    'Blowkiss',
    'Waddle',
    'Tremble',
    'Aaagh!',
    'Twirl',
    'Kotow',
    'Dramatic',
    'JumpRope',
    'Surrender',
]


_WECHAT_EMOJI_ZHCN = [
    '微笑',
    '撇嘴',
    '色',
    '发呆',
    '得意',
    '流泪',
    '害羞',
    '闭嘴',
    '睡',
    '大哭',
    '尴尬',
    '发怒',
    '调皮',
    '呲牙',
    '惊讶',
    '难过',
    '酷',
    '冷汗',
    '抓狂',
    '吐',
    '偷笑',
    '愉快',
    '白眼',
    '傲慢',
    '饥饿',
    '困',
    '惊恐',
    '流汗',
    '憨笑',
    '悠闲',
    '奋斗',
    '咒骂',
    '疑问',
    '嘘',
    '晕',
    '疯了',
    '衰',
    '骷髅',
    '敲打',
    '再见',
    '擦汗',
    '抠鼻',
    '鼓掌',
    '糗大了',
    '坏笑',
    '左哼哼',
    '右哼哼',
    '哈欠',
    '鄙视',
    '委屈',
    '快哭了',
    '阴险',
    '亲亲',
    '吓',
    '可怜',
    '菜刀',
    '西瓜',
    '啤酒',
    '篮球',
    '乒乓',
    '咖啡',
    '饭',
    '猪头',
    '玫瑰',
    '凋谢',
    '嘴唇',
    '爱心',
    '心碎',
    '蛋糕',
    '闪电',
    '炸弹',
    '刀',
    '足球',
    '瓢虫',
    '便便',
    '月亮',
    '太阳',
    '礼物',
    '拥抱',
    '强',
    '弱',
    '握手',
    '胜利',
    '抱拳',
    '勾引',
    '拳头',
    '爱你',
    'NO',
    'OK',
    '爱情',
    '飞吻',
    '跳跳',
    '发抖',
    '怄火',
    '转圈',
    '磕头',
    '回头',
    '跳绳',
    '投降',
]


def _create_wechat_emoji_regex(words):
    return r'|'.join(map(
        lambda x: r'\[{0}\]'.format(x),
        words,
    ))


WECHAT_EMOJI_EN = RegexProcessor(
    _create_wechat_emoji_regex(_WECHAT_EMOJI_EN),
)

WECHAT_EMOJI_ZHCN = RegexProcessor(
    _create_wechat_emoji_regex(_WECHAT_EMOJI_ZHCN),
)

WECHAT_EMOJI = RegexProcessor(
    _create_wechat_emoji_regex(_WECHAT_EMOJI_EN + _WECHAT_EMOJI_ZHCN),
)
