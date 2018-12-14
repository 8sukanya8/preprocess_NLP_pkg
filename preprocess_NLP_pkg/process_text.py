"""This file contains functions for manipulating text
"""

import re

def tokenize(character_seq, delimiter, remove_chars = None):
    """Removes given characters from a character sequence and splits according to the given delimiter
        character_seq -- character sequence to be split
        delimiter -- to split the character sequence
        remove_chars = the characters to remove
    """
    if remove_chars.len is not None:
        for i in remove_chars:
            re.sub(i, "", character_seq)
    tokens = character_seq.split(delimiter)
    return tokens