# encoding=utf-8
"""
Just some super-basic tests to see that everything is working as expected.
We should extend this to something more comprehensive soon.

The way to run this right now is to make your current directory the parent of the project directory, and then run:

    python -m mafan.tests.text_test

This places the mafan package on the relative path of this file.
"""

import random
import unittest
from six import unichr

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

    def generate_random_text(self, start, stop, length):
        """Generates a random string of unicode values between start and stop.

        Parameters:
            start: integer value corresponding to a unicode code point
            stop: integer value corresponding to a unicode code point
            length: the target length of the generated string

        """
        text = ''
        for n in range(1, length):
            text += unichr(random.randint(start, stop))
        return text

    def test_chinese_only(self):
        text = self.generate_random_text(19968, 40959, 20)
        self.assertFalse(contains_ascii(text))

    def test_printable_ascii_only(self):
        text = self.generate_random_text(32, 126, 20)
        self.assertTrue(contains_ascii(text))

    def test_non_printable_ascii_only(self):
        text = self.generate_random_text(0, 31, 20)
        self.assertFalse(contains_ascii(text))

    def test_chinese_and_ascii(self):
        text = self.generate_random_text(32, 126, 20)
        text += self.generate_random_text(19968, 40959, 20)
        self.assertTrue(contains_ascii(text))

    def test_empty_string(self):
        self.assertFalse(contains_ascii(''))


class TestSplitTextFunction(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(split_text(u"這是麻煩啦"), [u'這', u'是', u'麻煩', u'啦'])

if __name__ == '__main__':
    unittest.main()
