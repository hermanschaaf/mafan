# -*- coding: utf-8 -*-
"""The test module for Hanzi Identifier."""

import unittest

import hanzidentifier


class TestIdentifyFunction(unittest.TestCase):

    def test_return_none(self):
        text = 'Hello my name is Thomas.'
        self.assertIsNone(hanzidentifier.identify(text))

    def test_return_simp(self):
        text = u'Thomas 说：你好！'
        self.assertEqual(hanzidentifier.identify(text), hanzidentifier.SIMP)

    def test_return_trad(self):
        text = u'Thomas 說：你好！'
        self.assertEqual(hanzidentifier.identify(text), hanzidentifier.TRAD)

    def test_return_either(self):
        text = u'你好！'
        self.assertEqual(hanzidentifier.identify(text), hanzidentifier.EITHER)

    def test_return_both(self):
        text = u'Country in simplified: 国. Country in traditional: 國'
        self.assertEqual(hanzidentifier.identify(text), hanzidentifier.BOTH)

if __name__ == '__main__':
    unittest.main()
