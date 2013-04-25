===========
Mafan - Toolkit for working with Chinese in Python
===========

Mafan is a collection of Python tools for making your life working with Chinese so much less 麻烦 (mafan, i.e. troublesome). 

Contained in here is an ever-growing collection of loosely-related tools, broken down into several files. These are:

installation
===========

Install through pip:

    pip install mafan

encodings
===========

`encodings` contains functions for converting files from any number of 麻烦 character encodings to something more sane (utf-8, by default). For example:

    from mafan import encoding

    filename = 'ugly_big5.txt' # name or path of file as string
    encoding.convert(filename) # creates a file with name 'ugly_big5_utf-8.txt' in glorious utf-8 encoding


text
===========

`text` contains some functions for working with strings. Things like detecting english in a string, whether a string has Chinese punctuation, etc. Check out `text.py` for all the latest goodness. It also contains a handy wrapper for the jianfan package for converting between simplified and traditional:

    >>> from mafan import simplify, tradify
    >>> string = u'这是麻烦啦'
    >>> print tradify(string) # convert string to traditional
    這是麻煩啦
    >>> print simplify(tradify(string)) # convert back to simplified
    这是麻烦啦

The `has_punctuation` and `contains_latin` functions are useful for knowing whether you are really dealing with Chinese, or Chinese characters:

    >>> from mafan import text
    >>> text.has_punctuation(u'这是麻烦啦') # check for any Chinese punctuation (full-stops, commas, quotation marks, etc)
    False
    >>> text.has_punctuation(u'这是麻烦啦.')
    False
    >>> text.has_punctuation(u'这是麻烦啦。')
    True
    >>> text.contains_latin(u'这是麻烦啦。')
    False
    >>> text.contains_latin(u'You are麻烦啦。')
    True

You can also test whether sentences or documents use simplified characters, traditional characters, both or neither:

    >>> import mafan
    >>> from mafan import text
    >>> text.is_simplified(u'这是麻烦啦')
    True
    >>> text.is_traditional(u'Hello,這是麻煩啦') # ignores non-chinese characters
    True

    # Or done another way:
    >>> text.identify(u'这是麻烦啦') is mafan.SIMPLIFIED
    True
    >>> text.identify(u'這是麻煩啦') is mafan.TRADITIONAL
    True
    >>> text.identify(u'这是麻烦啦! 這是麻煩啦') is mafan.BOTH
    True
    >>> text.identify(u'This is so mafan.') is mafan.NEITHER # or None
    True

The identification functionality is introduced as a very thin wrapper to Thomas Roten's [hanzidentifier](https://github.com/tsroten/hanzidentifier), which is included as part of mafan.

pinyin
===========

`pinyin` contains functions for working with or converting between pinyin. At the moment, the only function in there is one to convert numbered pinyin to the pinyin with correct tone marks. For example:

    >>> from mafan import pinyin
    >>> print pinyin.decode("ni3hao3")
    nǐhǎo

settings
===========

Contributors:
-----------
 * Herman Schaaf ([IronZebra.com](http://www.ironzebra.com)) (Author)

Any contributions are very welcome! 


Sites using this:
-----------
 * [ChineseLevel.com](http://www.ChineseLevel.com)