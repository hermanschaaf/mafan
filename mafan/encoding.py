"""
Convert a file to utf-8 (or any encoding you want, really)
"""

__author__ = 'Herman Schaaf'
__version__ = '0.3'

import os
import sys
import subprocess
import logging
import chardet

logging.basicConfig(level=logging.ERROR)


def convert(filename, new_filename=None, overwrite=False, to_encoding='utf-8', force=True):
    """ Convert file with crappy encoding to a new proper encoding (or vice versa if you wish).

    filename -- the name, partial path or full path of the file you want to encode to a new encoding
    new_filename -- (optional) the name of the new file to be generated using the new encoding
    overwrite -- if `new_filename` is omitted, set this to True to change the supplied file's 
               encoding and not bother creating a new file (be careful! loss of information is likely)
    to_encoding -- the name of the encoding you wish to convert to (utf-8 by default)
    force -- Encode even if the current file is already in the correct encoding.
    """
    logging.info('Opening file %s' % filename)
    f = open(filename)
    detection = chardet.detect(f.read())
    f.close()
    encoding = detection.get('encoding')
    confidence = detection.get('confidence')
    logging.info('I think it is %s with %.1f%% confidence' % (encoding, confidence * 100.0))

    delete_original = bool(new_filename) == False and overwrite
    if not new_filename or new_filename == filename:
        # use the current filename, but add the encoding to the name (while keeping extension intact)
        base_name, ext = os.path.splitext(filename)
        new_filename = base_name + '_%s' % to_encoding + ext

    if not encoding.lower() == to_encoding.lower():
        logging.info('Converting to %s with iconv...' % to_encoding)
    else:
        logging.info('Already in correct encoding.')
        if force:
            logging.info('Going ahead anyway, because force == True (the force is strong with this one)')
        else:
            logging.warning('Stopping. Use force = True if you want to force the encoding.')
            return None

    # command example: iconv -f gb18030 -t utf-8 chs.srt > chs-utf8.srt
    # "iconv" does not support -o parameter now and use stdout to instead.
    with open(new_filename, 'w') as output_file:
        p = subprocess.Popen(['iconv', '-f', encoding, '-t', to_encoding + "//IGNORE", \
                os.path.abspath(filename)], shell=False, \
                stdout=output_file, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
        retval = p.wait()

    if delete_original and os.path.isfile(new_filename):
        os.remove(filename)
        os.rename(new_filename, filename)
        new_filename = filename

    return new_filename


def detect(filename, include_confidence=False):
    """
    Detect the encoding of a file.

    Returns only the predicted current encoding as a string.

    If `include_confidence` is True, 
    Returns tuple containing: (str encoding, float confidence)
    """
    f = open(filename)
    detection = chardet.detect(f.read())
    f.close()
    encoding = detection.get('encoding')
    confidence = detection.get('confidence')
    if include_confidence:
        return (encoding, confidence)
    return encoding
