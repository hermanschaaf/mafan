# -*- coding: utf-8 -*-
# author: Leon Dong <Leon.Dong@gmail.com>
# commiter: Thomas <tsroten@gmail.com>

"""
    Jianfan is a library for translation between traditional and simplified chinese.
    Support Python 2 and Python 3. Thanks for Thomas to provide Python 3 support.
        two functions are provided by the library:
        jtof: translate simplified chinese to traditional chinese
        jtoj: translate traditional chinese to simplified chinese
        the two functions accept one parameter that is unicode or string
        the type of return value is unicode

    Jianfan是一个简体中文和繁体中文转换的库。提供了两个函数：
        jtof: 简体转换为繁体
        ftoj: 繁体转换为简体
        函数接受unicode和string类型作为参数，返回值统一为unicode
"""

from charsets import gbk, big5

def _t(unistr, charset_from, charset_to):
    """
        This is a unexposed function, is responsibility for translation internal.
    """
    if type(unistr) is str:
        try:
            unistr = unistr.decode('utf-8')
        # Python 3 returns AttributeError when .decode() is called on a str
        # This means it is already unicode.
        except AttributeError:
            pass
    try:
        if type(unistr) is not unicode:
            return unistr
    # Python 3 returns NameError because unicode is not a type.
    except NameError:
        pass

    chars = []
    for c in unistr:
        idx = charset_from.find(c)
        chars.append(charset_to[idx] if idx!=-1 else c)
    return u''.join(chars)


def jtof(unicode_string):
    """
        Translate simplified chinese to traditional chinese.
        >>> s = u'中华'
        >>> print jtof(s)
        中華
    """
    return _t(unicode_string, gbk, big5)

def ftoj(unicode_string):
    """
        Translate traditional chinese to simplified chinese.
        >>> t = u'中華'
        >>> print ftoj(t)
        中华
    """
    return _t(unicode_string, big5, gbk)
