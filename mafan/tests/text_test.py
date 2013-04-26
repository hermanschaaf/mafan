#encoding=utf-8
"""
Just some super-basic tests to see that everything is working as expected.
We should extend this to something more comprehensive soon.

The way to run this right now is to make your current directory the parent of the project directory, and then run:

    python -m mafan.tests.text_test

This places the mafan package on the relative path of this file.
"""

import random
import unittest

from ..text import *

st = u"聲音鳥樹葉話説話細又輕蝴蝶請只有和得聼得到蜜蜂"
st2 = u'这是麻烦啦'

class TestIdentifyFunction(unittest.TestCase):

    def test_simplify(self):
        self.assertEqual(simplify(st2), st2)

    def test_tradify(self):
        self.assertEqual(tradify(st2), u'這是麻煩啦')

    def test_simplify_and_tradify(self):
        self.assertEqual(simplify(tradify(st2)), st2)

class TestContainsAsciiFunction(unittest.TestCase):

    def test_chinese_only(self):
        text = ''
        for n in range(0,20):
            text += unichr(random.randint(19968, 40959))
        self.assertFalse(contains_ascii(text))

    def test_printable_ascii_only(self):
        text = ''
        for n in range(0,20):
            text += unichr(random.randint(32, 126))
        self.assertTrue(contains_ascii(text))

    def test_non_printable_ascii_only(self):
        text = ''
        for n in range(0,20):
            text += unichr(random.randint(0, 31))
        self.assertFalse(contains_ascii(text))

    def test_chinese_and_ascii(self):
        text = ''
        for n in range(0,20):
            text += unichr(random.randint(32, 126))
            text += unichr(random.randint(19968, 40959))
        self.assertTrue(contains_ascii(text))

if __name__ == '__main__':
    unittest.main()
