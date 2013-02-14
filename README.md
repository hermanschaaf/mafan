===========
Mafan - Toolbelt for working with Chinese in Python
===========

Mafan is a collection of Python tools for making your life working with Chinese so much less 麻烦 (mafan, i.e. troublesome). 

Contained in here is an ever-growing collection of loosely-related tools, broken down into several files. These are:

encodings
===========

`encodings` contains functions for converting files from any number of 麻烦 character encodings to something more sane (utf-8, by default). For example:

    from mafan import encoding

    filename = 'ugly_big5.txt' # name or path of file as string
    encoding.convert(filename) # creates a file with name 'ugly_big5_utf-8.txt' in glorious utf-8 encoding


Any contributions are welcome!


Contributors:
-----------
Herman Schaaf [IronZebra.com](http://www.ironzebra.com)