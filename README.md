# text-cleaner, simple text preprocessing tool

## Introduction

* Support Python 2.7 - 3.x.
* Simple interfaces.
* Easy to extend.

## Usage

```python
from text_cleaner import remove, keep

from text_cleaner.processor.common import ASCII
from text_cleaner.processor.chinese import CHINESE
from text_cleaner.processor.misc import URL

# remove url and ascii characters.
# return: u'点击  查看 '
remove(
    '点击http://t.cn/RtU0mZ1 查看,123456,test',
    [URL, ASCII],
)

# keep chinese characters and url.
# return: u'点击 http://t.cn/RtU0mZ1 查看'
keep(
    '点击http://t.cn/RtU0mZ1 查看,123456,test',
    [CHINESE, URL],
)

# use processor directly.
# return: u'点击  查看'
URL.remove('点击http://t.cn/RtU0mZ1 查看')
# return: u'点击<URL> 查看'
URL.replace('<URL>').remove('点击http://t.cn/RtU0mZ1 查看')
```

## Interfaces

*text_cleaner.remove(text, processors)*:

* *text*: `str` or `bytes` (`unicode` or `str` for Python 2).
* *processors*: iterable of processors. *remove* invokes `remove` of each processor to handle *text*.

*text_cleaner.keep(text, processors)*:

* same as *remove*, but invoke `keep` method of processors instead.

## Processors

*DEFAULT\_REPLACE\_TEXT*: `' '`, single space.

*RegexProcessor(regex, replace\_text=DEFAULT\_REPLACE\_TEXT)*

* contruct a regex processor for *regex*, replace unmatched components with *replace\_text*.
* *replace(self, new\_replace\_text)*: create a new processor, with new *replace\_text* is set.
* *remove(self, text)*: remove all occurences of *regex* from *text*.
* *keep(self, text)*: keep only the occurences of *regex*, remove all unmatched components from *text*.
* *verify(self, text)*: return *True* if text match *regex*, otherwise returns *False*.

*UnicodeRange(begin, end)*:

* *begin*: *int*, the begin of unicode range.
* *end*: *int*, the end of unicode range.

*UnicodeRangeProcessor(ranges, replace\_text=DEFAULT\_REPLACE\_TEXT)*

* subclass of *RegexProcessor*.
* *ranges*: iterable of instances of *UnicodeRange*.

## Built-in Processors

Following processors are defined by *UnicodeRange* and regex. Read the source code if you are sure about what's going on.

`text_cleaner.processor.common`, for common usage:

* `ALPHA`
* `DIGIT`
* `SYMBOLS_AND_PUNCTUATION`
* `ASCII`
* `ALPHA_EXTENSION`
* `DIGIT_EXTENSION`
* `SYMBOLS_AND_PUNCTUATION_EXTENSION`

`text_cleaner.processor.misc`, misellanious processors:

* `URL`
* `ESCAPED_WHITESPACE`

`text_cleaner.processor.chinese`, Chinese processing:

* `CHINESE_CHARACTER`: only common characters.
* `CHINESE`: common characters + symbols and puntuations.
* `CHINESE_ALL`: all CJK characters.
* `CHINESE_EXTENSION`
* `CHINESE_COMPATIBILITY`
* `CHINESE_SYMBOLS_AND_PUNCTUATION_RANGES`
