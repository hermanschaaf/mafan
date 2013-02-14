#encoding=utf-8
"""
Some helpful functions for parsing or changing Chinese text
"""
import re
from HTMLParser import HTMLParser

from jianfan import jtof as tradify, ftoj as simplify
to_traditional = tradify
to_simplified = simplify

english = re.compile('[\w\~\!\s\@\#\$\%\^\&\*\(\)]+')
known_punctuation = u'／（）、，。：「」…。'

def contains_english(unicode_string):
  """Attempts to determine whether the string contains any of the common English characters."""
  
  if english.search(unicode_string):
    return True
  return False


def contains_latin(unicode_string):
  """Attempts to determine whether the string contains any non-Asian scripts"""
  string = unicode_string.encode("ascii", "ignore")
  return contains_english(string)


def is_punctuation(word):
  """
  Check if a string is among any of the common Chinese punctuation.
  """
  return word in known_punctuation
