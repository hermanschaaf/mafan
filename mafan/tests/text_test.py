#encoding=utf-8
"""
Just some super-basic tests to see that everything is working as expected.
We should extend this to something more comprehensive soon.

The way to run this right now is to make your current directory the parent of the project directory, and then run:

    python -m mafan.tests.text_test

This places the mafan package on the relative path of this file.
"""


from ..text import *


st = u"聲音鳥樹葉話説話細又輕蝴蝶請只有和得聼得到蜜蜂"
st2 = u'这是麻烦啦'


print "Testing %s ..." % "test"
print "is_simplified: %s" % is_simplified("test")

print "Testing %s ..." % st
print "is_simplified: %s" % is_simplified(st)
assert is_simplified(st) == False, "Failed test: is_simplified"
print "is_traditional: %s" % is_traditional(st)
assert is_traditional(st) == True, "Failed test: is_traditional"

print "Testing %s ..." % st2
print "is_simplified: %s" % is_simplified(st2)
assert is_simplified(st2) == True, "Failed test: is_simplified2"
print "is_traditional: %s" % is_traditional(st2)
assert is_traditional(st2) == False, "Failed test: is_traditional2"

print "Passed simplified and traditional tests."

assert tradify(st2) == u'這是麻煩啦', "Failed test: tradify"
assert simplify(st2) == st2, "Failed test: simplify"
assert simplify(tradify(st2)) == st2, "Failed test: text -> tradify -> simplify"

print "Passed all tests!"