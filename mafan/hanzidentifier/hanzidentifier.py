"""Python module that identifies Chinese text as simplified or traditional.

Constants:
    TRAD: The value returned by identify() when the text is recognized as
        traditional.
    SIMP: The value returned by identify() when the text is recognized as
        simplified.
    EITHER: The value returned by identify() when the text is recognized as
        being either simplified or traditional (inconclusive).
    BOTH: The value returned by identify() when the text is recognized as
        having both simplified and traditional characters.
    TRAD_CHARS: a set of characters recognized as traditional.
    SIMP_CHARS: a set of characters recognized as simplified.
    SHARED_CHARS: a set of characters recognized in simplified and traditional
        writing.
    ALL_CHARS: a set representing traditional and simplified characters.

Functions:
    identify: identify whether a text is simplified or traditional.

"""

from .data import TRAD as data_TRAD
from .data import SIMP as data_SIMP

TRAD = 0
SIMP = 1
EITHER = 2
BOTH = 3

TRAD_CHARS = set(list(data_TRAD))
SIMP_CHARS = set(list(data_SIMP))

SHARED_CHARS = TRAD_CHARS.intersection(SIMP_CHARS)
ALL_CHARS = TRAD_CHARS.union(SIMP_CHARS)


def identify(text):
    """Identify whether a string is simplified or traditional Chinese.

    Returns:
        None: if there are no recognizd Chinese characters.
        EITHER: if the test is inconclusive.
        TRAD: if the text is traditional.
        SIMP: if the text is simplified.
        BOTH: the text has characters recognized as being solely traditional
            and other characters recognized as being solely simplified.

    """
    filtered_text = set(list(text)).intersection(ALL_CHARS)
    if len(filtered_text) is 0:
        return None
    if filtered_text.issubset(SHARED_CHARS):
        return EITHER
    if filtered_text.issubset(TRAD_CHARS):
        return TRAD
    if filtered_text.issubset(SIMP_CHARS):
        return SIMP
    if filtered_text.difference(TRAD_CHARS).issubset(SIMP_CHARS):
        return BOTH
