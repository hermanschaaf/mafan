Hanzi Identifier
================

About
-----

Hanzi Identifier is a simple Python module that identifies a string of text has having simplified or traditional characters.

There are five possible return values:

* None: there are no recognized Chinese characters in the string.
* hanzidentifier.EITHER: the string could be simplified or traditional -- the test is inconclusive.
* hanzidentifier.TRAD: the string consists of traditional characters.
* hanzidentifier.SIMP: the string consists of simplified characters.
* hanzidentifier.BOTH: the string consists of characters recognized solely as traditional characters and also consists of characters recognized solely as simplified characters.

```python
>>> import hanzidentifier
>>> hanzidentifier.identify('Hello my name is Thomas.') is None
True
>>> hanzidentifier.identify(u'Thomas 说：你好！') is hanzidentifier.SIMP
True
>>> hanzidentifier.identify(u'Thomas 說：你好！') is hanzidentifier.TRAD
True
>>> hanzidentifier.identify(u'你好！') is hanzidentifier.EITHER
True
>>> hanzidentifier.identify(u'Country in simplified: 国家. Country in traditional: 國家' ) is hanzidentifier.BOTH
True
```

License
-------

Hanzi Identifier is released under the OSI-approved [MIT License](http://opensource.org/licenses/MIT). See the file LICENSE.txt for more information.
