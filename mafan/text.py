# -*- coding: utf-8 -*-
"""
Some helpful functions for parsing or changing Chinese text
"""
import re
import os
import subprocess
from HTMLParser import HTMLParser

import jieba
import jieba.posseg as pseg

from constants import SIMPLIFIED, TRADITIONAL, EITHER, BOTH, NEITHER

from hanzidentifier import hanzidentifier

_curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) ))
settings_path = os.environ.get('MAFAN_DICTIONARY_PATH')
if settings_path and os.path.exists(settings_path):
    jieba.set_dictionary(settings_path)
elif os.path.exists(os.path.join(_curpath, 'data/dict.txt.big')):
    jieba.set_dictionary('data/dict.txt.big')
else:
    try:
        import mafan_traditional
        jieba.set_dictionary(mafan_traditional.path)
        print "Using traditional dictionary!"
    except ImportError:
        pass

from jianfan import jtof as tradify, ftoj as simplify
to_traditional = tradify
to_simplified = simplify

known_stops = u'。。…！？'
known_punctuation = u'／（）、，。：「」…。『』！？《》“”；’ ‘【】·〔〕'

re_split_sentences = re.compile(r"[%s]+" % known_stops)


def contains_ascii(unicode_string):
    u"""Attempts to determine whether the string contains any ASCII characters.

    Checks for any printable ASCII characters (0020-007E).

    It does not check for non-printable ASCII characters such as tabs and spaces,
        because those are often present in Chinese typing as well.

    :TODO: Tests
    """
    if re.search(ur'[\u0020-\u007E]', unicode_string) is None:
            return False
    else:
            return True


def contains_latin(unicode_string):
    u"""
    Kept for backwards-compatibility.

    :TODO: Improve this to also look for characters
    such as ô,ê,ā,ɛ, etc.
    """
    return contains_ascii(unicode_string)


def contains_english(unicode_string):
    u"""
    Kept for backwards-compatibility.
    Just a wrapper for contains_ascii
    """
    return contains_ascii(unicode_string)

def contains_chinese(unicode_string):
    u"""
    Check whether the given unicode string contains any chinese characters.
    >>> contains_chinese(u'Hello,這是麻煩啦')
    True
    >>> contains_chinese(u'Hello')
    False
    >>> contains_chinese(u'。…！？') # punctuation does not count as Chinese
    False
    """
    if re.search(ur'[\u4E00-\u9FFF]+', unicode_string) is None:
        return False
    else:
        return True


def has_punctuation(word):
    u"""
    Check if a string has any of the common Chinese punctuation marks.
    """
    if re.search(r'[%s]' % known_punctuation, word) is not None:
            return True
    else:
            return False


def is_punctuation(character):
    u"""Tells whether the supplied character is a Chinese punctuation mark.

    This is useful for filtering out punctuation, for example.

    >>> sentence = u"你的電子郵件信箱「爆」了！無法寄信給你。"
    >>> print filter(lambda c: not is_punctuation(c), sentence)
    你的電子郵件信箱爆了無法寄信給你

    >>> word = u"『爆』？"
    >>> is_punctuation(word[0])
    True
    >>> is_punctuation(word[1])
    False
    >>> all(map(is_punctuation, word[2:]))
    True
    """
    return has_punctuation(character)


def iconv(text, args):
    p1 = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['iconv'] + list(args), stdout=subprocess.PIPE, stdin = p1.stdout, stderr=subprocess.STDOUT)
    p1.stdout.close()
    output = p2.communicate()[0]
    print output
    return output


def identify(text):
    u"""
    Wrapper for hanzidentifier identify function

    Returns:
        None: if there are no recognizd Chinese characters.
        EITHER: if the test is inconclusive.
        TRADITIONAL: if the text is traditional.
        SIMPLIFIED: if the text is simplified.
        BOTH: the text has characters recognized as being solely traditional
                and other characters recognized as being solely simplified.
        NEITHER: (or None) It's neither simplified nor traditional Chinese text.

    >>> identify(u'这是麻烦啦') is SIMPLIFIED
    True
    >>> identify(u'這是麻煩啦') is TRADITIONAL
    True
    >>> identify(u'这是麻烦啦! 這是麻煩啦') is BOTH
    True
    >>> identify(u'This is so mafan.') is NEITHER
    True
    """
    return hanzidentifier.identify(text)


def is_simplified(text):
    u"""
    Determine whether a text is simplified Chinese
    Returns True if written in Simplified, False otherwise.

    Note: This assumes the text is known to be one or the other.

    >>> is_simplified(u'这是麻烦啦')
    True

    """
    return hanzidentifier.identify(text) is SIMPLIFIED


def is_traditional(text):
    u"""
    Determine whether a text is simplified Chinese
    Returns True if written in Simplified, False otherwise.

    Note: This assumes the text is known to be one or the other.

    >>> is_traditional(u'Hello,這是麻煩啦')
    True

    """
    return hanzidentifier.identify(text) is TRADITIONAL


def is_chinese(text):
    u"""
    Determine whether the entire string contains only Chinese characters.
    This checks every character, so it is pretty slow - try to use only on
    short sentences or words.

    >>> is_chinese(u'這是麻煩啦')
    True
    >>> is_chinese(u'Hello,這是麻煩啦')
    False
    >>> is_chinese(u'♪')
    False
    """
    return all([c in hanzidentifier.ALL_CHARS for c in text])


def _is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def split_text(text, include_part_of_speech=False, strip_english=False, strip_numbers=False):
    u"""
    Split Chinese text at word boundaries.

    include_pos: also returns the Part Of Speech for each of the words.
    Some of the different parts of speech are:
        r: pronoun
        v: verb
        ns: proper noun
        etc...

    This all gets returned as a tuple:
        index 0: the split word
        index 1: the word's part of speech

    strip_english: remove all entries that have English or numbers in them (useful sometimes)
    """

    if not include_part_of_speech:
        seg_list = pseg.cut(text)
        if strip_english:
            seg_list = filter(lambda x: not contains_english(x), seg_list)
        if strip_numbers:
            seg_list = filter(lambda x: not _is_number(x), seg_list)
        return list(map(lambda i: i.word, seg_list))
    else:
        seg_list = pseg.cut(text)
        objs = map(lambda w: (w.word, w.flag), seg_list)
        if strip_english:
            objs = filter(lambda x: not contains_english(x[0]), objs)
        if strip_english:
            objs = filter(lambda x: not _is_number(x[0]), objs)
        return objs

    # if was_traditional:
    #   seg_list = map(tradify, seg_list)

    return list(seg_list)


def split_sentences(text):
    u"""
    Split Chinese text into a list of sentences, separated by punctuation.

    >>> sentence = u"你的電子郵件信箱「爆」了！無法寄信給你。我知道，我正在刪除信件中。"
    >>> print '_'.join(split_sentences(text=sentence))
    你的電子郵件信箱「爆」了_無法寄信給你_我知道，我正在刪除信件中
    """
    s = list(text)
    return filter(None, re.split(re_split_sentences, text))


if __name__ == "__main__":
        import doctest
        doctest.testmod()
