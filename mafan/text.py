#encoding=utf-8
"""
Some helpful functions for parsing or changing Chinese text
"""
import re
import subprocess
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
  Check if a string is among any of the common Chinese punctuation marks.
  """
  return word in known_punctuation


def has_punctuation(word):
  """
  Check if a string has any of the common Chinese punctuation marks.
  """
  # this could be more efficient
  return any(is_punctuation(c) for c in word)


def iconv(text, args):
  p1 = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
  p2 = subprocess.Popen(['iconv'] + list(args), stdout=subprocess.PIPE, stdin = p1.stdout, stderr=subprocess.STDOUT)
  p1.stdout.close()
  output = p2.communicate()[0]
  print output
  return output


def is_simplified(text):
  """
  Determine whether a text is simplified Chinese
  Returns True if written in Simplified, False otherwise.

  Note: This assumes the text is known to be one or the other.
  """

  # TODO: Write a nice(r) wrapper for iconv

  print "big5 - 1"
  test1 = iconv(text, args=['-f', "UTF-8", '-t', "big5//TRANSLIT", "-s", "-c"])
  print "big5 - 2"
  test2 = iconv(text, args=['-f', "UTF-8", '-t', "big5//IGNORE", "-s", "-c"])

  if test1 == test2:
     return False
  else:
     test3 = iconv(text, args=["-f", "UTF-8", "-t", "gb18030//TRANSLIT", "-s", "-c"])
     test4 = iconv(text, args=["-f", "UTF-8", "-t", "gb18030//IGNORE", "-s", "-c"])
     if test3 == test4:
        return True
     else:
        return None


def is_traditional(text):
  """
  Determine whether a text is simplified Chinese
  Returns True if written in Simplified, False otherwise.

  Note: This assumes the text is known to be one or the other.
  """
  simp = is_simplified(text)
  if simp is None: 
    return None
  else: 
    return not simp